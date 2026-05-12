import os
import io
import torch
import torchvision.transforms as T
import numpy as np
from PIL import Image
import tensorflow as tf
from dotenv import load_dotenv

load_dotenv()

# --- Model Configurations ---
MODEL_44_PATH = "backend/models/brain_tumor_efficientnetv2_s_finetuned.h5"
MODEL_17_PATH = "backend/models/brain_tumor_convnext_tiny_scripted.pt"
CLASS_LABELS_44 = [
    'Astrocitoma (Grado II)', 'Astrocitoma (Grado III)', 'Astrocitoma (Grado IV)',
    'Carcinoma', 'Ependimoma (Grado II)', 'Ependimoma (Grado III)',
    'Ganglioglioma (Grado I)', 'Ganglioglioma (Grado II)', 'Germinoma',
    'Glioblastoma (Grado IV)', 'Granuloma', 'Meduloblastoma (Grado IV)',
    'Meningioma (Grado I)', 'Meningioma (Grado II)', 'Meningioma (Grado III)',
    'Neurocitoma (Grado II)', 'Oligodendroglioma (Grado II)', 'Oligodendroglioma (Grado III)',
    'Papiloma (Grado I)', 'Papiloma (Grado II)', 'Papiloma (Grado III)',
    'Schwannoma (Grado I)', 'Schwannoma (Grado II)', 'Tuberculoma', 'Normal'
]
# Note: Simplified for display, using indices for others. 
# We'll use these labels for the top 3.
CLASS_LABELS_17 = ["Glioma", "Meningioma", "Neurocytoma", "Other Injuries", "Schwannoma", "Normal"]

# Global model placeholders
model_44 = None
model_17 = None
medgemma_processor = None
medgemma_model = None

# --- ZeroGPU Integration ---
try:
    import spaces
    HAS_SPACES = True
except ImportError:
    HAS_SPACES = False

def gpu_decorator(func):
    if HAS_SPACES:
        return spaces.GPU(func)
    return func

def load_tumor_models():
    """Load both diagnostic models into memory."""
    global model_44, model_17
    
    # Load 44-class (TensorFlow)
    if os.path.exists(MODEL_44_PATH):
        try:
            model_44 = tf.keras.models.load_model(MODEL_44_PATH)
            print("Loaded 44-class model.")
        except Exception as e:
            print(f"Error loading 44-class model: {e}")

    # Load 17-class (PyTorch)
    if os.path.exists(MODEL_17_PATH):
        try:
            model_17 = torch.jit.load(MODEL_17_PATH)
            model_17.eval()
            print("Loaded 17-class model.")
        except Exception as e:
            print(f"Error loading 17-class model: {e}")

def preprocess_image(image_bytes, model_type):
    """Preprocess image based on model requirements."""
    img = Image.open(image_bytes).convert('RGB')
    if model_type == "44BTIS":
        img = img.resize((224, 224))
        img_array = np.array(img)
        return np.expand_dims(img_array, axis=0)
    else:
        preprocess = T.Compose([
            T.Resize((224, 224)),
            T.ToTensor(),
            T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        return preprocess(img).unsqueeze(0)

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
        prompt = (
            f"System: You are a senior neuroradiologist. Verify this MRI prediction.\n"
            f"User: Prediction results: {prediction_results}. "
            f"Please provide a 1-sentence final diagnosis and a brief radiological explanation."
        )
        
        messages = [{"role": "user", "content": [{"type": "image", "image": image}, {"type": "text", "text": prompt}]}]
        
        inputs = medgemma_processor.apply_chat_template(
            messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt"
        ).to(medgemma_model.device, dtype=torch.bfloat16)

        with torch.inference_mode():
            generation = medgemma_model.generate(**inputs, max_new_tokens=256, do_sample=False)
            response = medgemma_processor.decode(generation[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)

        return {
            "verified_answer": response.split('.')[0] + '.', 
            "explanation": response.strip()
        }

    except Exception as e:
        return {
            "verified_answer": "Verification Unavailable", 
            "explanation": f"MedGemma error: {str(e)}"
        }

def predict_tumor(image_bytes: io.BytesIO, model_type: str = "44BTIS", run_verification: bool = False) -> dict:
    """Main prediction pipeline."""
    image_bytes.seek(0)
    image = preprocess_image(image_bytes, model_type)
    
    if model_type == "17ConVext":
        if model_17 is None: return {"error": "17-class model not loaded."}
        with torch.no_grad():
            output = model_17(image)
            probs = torch.softmax(output, dim=1)[0]
            # Map top indices
            top_3_vals, top_3_idx = torch.topk(probs, 3)
            predictions = [
                {"label": CLASS_LABELS_17[int(idx)] if int(idx) < len(CLASS_LABELS_17) else f"Type {idx}", 
                 "confidence": round(float(val) * 100, 2)} 
                for val, idx in zip(top_3_vals, top_3_idx)
            ]
    else:
        if model_44 is None: return {"error": "44-class model not loaded."}
        preds = model_44.predict(image)[0]
        top_3_idx = np.argsort(preds)[-3:][::-1]
        predictions = [
            {"label": CLASS_LABELS_44[int(idx)] if int(idx) < len(CLASS_LABELS_44) else f"Type {idx}", 
             "confidence": round(float(preds[idx]) * 100, 2)} 
            for idx in top_3_idx
        ]

    results = {"model_type": model_type, "predictions": predictions}

    if run_verification:
        pred_str = ", ".join([f"{p['label']} ({p['confidence']}%)" for p in predictions])
        image_bytes.seek(0)
        results["medgemma_verification"] = verify_with_medgemma(image_bytes, pred_str)

    return results
