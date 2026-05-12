# Backend functions and libraries — ported from modelpipeline.py
import os
import io

# ── CRITICAL: these must be set BEFORE importing tensorflow ──
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"       # Force CPU-only (no GPU on Render)
os.environ["TF_USE_LEGACY_KERAS"] = "1"          # Use Keras 2 API for .h5 compat
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"         # Suppress TF info/warning spam

import numpy as np
import tensorflow as tf
import torch
import torchvision.transforms as T
import requests
import base64
from PIL import Image
from dotenv import load_dotenv

# Optional ZeroGPU support
try:
    import spaces
except ImportError:
    # Dummy decorator for local dev
    class spaces:
        @staticmethod
        def GPU(func):
            return func

from transformers import AutoProcessor, AutoModelForImageTextToText, BitsAndBytesConfig

# Load environment variables (HF_TOKEN, etc.)
load_dotenv()

# ... (custom_objects remains the same)

# Model states
model_44 = None
model_17 = None
medgemma_model = None
medgemma_processor = None

# HF Configuration for MedGemma
HF_TOKEN = os.getenv("HF_TOKEN")
MEDGEMMA_MODEL_ID = "google/medgemma-1.5-4b-it" 

# ... (MODEL_PATHS remain the same)

# ... (CLASS_LABELS remain the same)

def load_tumor_model():
    """Load all ML models at startup."""
    global model_44, model_17, medgemma_model, medgemma_processor

    # Load 44-class (TensorFlow)
    if os.path.exists(MODEL_44_PATH):
        try:
            import tf_keras
            model_44 = tf_keras.models.load_model(MODEL_44_PATH, custom_objects=custom_objects, compile=False)
            model_44.compile(optimizer='Adamax', loss='categorical_crossentropy')
            print(f"44-class model loaded from {MODEL_44_PATH}")
        except Exception as e:
            print(f"Error loading 44-class model: {e}")

    # Load 17-class (PyTorch Scripted)
    if os.path.exists(MODEL_17_PATH):
        try:
            model_17 = torch.jit.load(MODEL_17_PATH)
            model_17.eval()
            print(f"17-class model loaded from {MODEL_17_PATH}")
        except Exception as e:
            print(f"Error loading 17-class model: {e}")

    # Load MedGemma 1.5 4B (Local Inference)
    if HF_TOKEN:
        try:
            print(f"Loading MedGemma 1.5 4B ({MEDGEMMA_MODEL_ID})...")
            quant_config = BitsAndBytesConfig(load_in_4bit=True)
            medgemma_processor = AutoProcessor.from_pretrained(MEDGEMMA_MODEL_ID, token=HF_TOKEN)
            medgemma_model = AutoModelForImageTextToText.from_pretrained(
                MEDGEMMA_MODEL_ID,
                token=HF_TOKEN,
                quantization_config=quant_config,
                device_map="auto",
                torch_dtype=torch.bfloat16
            )
            print("MedGemma 1.5 4B loaded successfully.")
        except Exception as e:
            print(f"Error loading MedGemma: {e}")

@spaces.GPU
def verify_with_medgemma(image_bytes: bytes, initial_prediction: str, confidence: float) -> str:
    """
    Use MedGemma 1.5 4B locally via ZeroGPU to verify the prediction.
    """
    if medgemma_model is None or medgemma_processor is None:
        return "Verification unavailable (MedGemma not loaded)."

    try:
        # Prepare image
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        
        # Standard VLM Prompt for Medical Verification
        prompt = (
            f"Analyze this brain MRI image. The classifier suggested '{initial_prediction}' "
            f"with {confidence}% confidence. As a medical imaging expert, provide a single final answer "
            f"stating the most probable tumor type and a brief explanation of the radiological signs "
            f"supporting this diagnosis."
        )

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image},
                    {"type": "text", "text": prompt}
                ]
            }
        ]

        inputs = medgemma_processor.apply_chat_template(
            messages, 
            add_generation_prompt=True, 
            tokenize=True, 
            return_dict=True, 
            return_tensors="pt"
        ).to(medgemma_model.device, dtype=torch.bfloat16)

        input_len = inputs["input_ids"].shape[-1]
        
        with torch.inference_mode():
            generation = medgemma_model.generate(
                **inputs, 
                max_new_tokens=250, 
                do_sample=False
            )
            generation = generation[0][input_len:]
            decoded = medgemma_processor.decode(generation, skip_special_tokens=True)
            
            return decoded.strip()
@gpu_decorator
def verify_with_medgemma(image_bytes: io.BytesIO, prediction_results: str) -> dict:
    """
    Runs MedGemma 1.5 4B for clinical verification using HF ZeroGPU.
    """
    global medgemma_processor, medgemma_model
    
    from transformers import AutoProcessor, AutoModelForImageTextToText
    import torch
    from PIL import Image

    model_id = "google/medgemma-1.5-4b-it"
    
    try:
        if medgemma_processor is None:
            medgemma_processor = AutoProcessor.from_pretrained(model_id)

        if medgemma_model is None:
            medgemma_model = AutoModelForImageTextToText.from_pretrained(
                model_id,
                torch_dtype=torch.bfloat16,
                device_map="auto",
                load_in_4bit=True
            )

        image = Image.open(image_bytes).convert("RGB")
        prompt = f"System: You are a senior neuroradiologist. Verify this MRI prediction.\nUser: Prediction results: {prediction_results}. Please provide a 1-sentence final diagnosis and a brief radiological explanation."
        
        messages = [{"role": "user", "content": [{"type": "image", "image": image}, {"type": "text", "text": prompt}]}]
        
        inputs = medgemma_processor.apply_chat_template(
            messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt"
        ).to(medgemma_model.device, dtype=torch.bfloat16)

        with torch.inference_mode():
            generation = medgemma_model.generate(**inputs, max_new_tokens=256, do_sample=False)
            response = medgemma_processor.decode(generation[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)

        return {"verified_answer": response.split('.')[0] + '.', "explanation": response}

    except Exception as e:
        return {"verified_answer": "Verification Unavailable", "explanation": f"MedGemma error: {str(e)}"}

def predict_tumor(image_bytes: io.BytesIO, model_type: str = "44BTIS", run_verification: bool = False) -> dict:
    """Main prediction pipeline."""
    image = preprocess_image(image_bytes, model_type)
    
    if model_type == "17ConVext":
        if model_17 is None: return {"error": "17-class model not loaded."}
        with torch.no_grad():
            output = model_17(image)
            probs = torch.softmax(output, dim=1)[0]
            confidences = {CLASS_LABELS_17[i]: float(probs[i]) for i in range(len(CLASS_LABELS_17))}
    else:
        if model_44 is None: return {"error": "44-class model not loaded."}
        preds = model_44.predict(image)[0]
        confidences = {CLASS_LABELS_44[i]: float(preds[i]) for i in range(len(CLASS_LABELS_44))}

    sorted_confs = sorted(confidences.items(), key=lambda x: x[1], reverse=True)
    top_3 = [{"label": k, "confidence": round(v * 100, 2)} for k, v in sorted_confs[:3]]
    
    results = {"model_type": model_type, "predictions": top_3}

    if run_verification:
        pred_str = ", ".join([f"{p['label']} ({p['confidence']}%)" for p in top_3])
        image_bytes.seek(0)
        results["medgemma_verification"] = verify_with_medgemma(image_bytes, pred_str)

    return results
