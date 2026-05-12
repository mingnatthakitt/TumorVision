import os
# Force legacy Keras before importing tensorflow to avoid lambda layer warning
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import io
import torch
import torchvision.transforms as T
import numpy as np
from PIL import Image
import tensorflow as tf
from dotenv import load_dotenv

load_dotenv()

# --- Custom Layer for EfficientNetV2 ---
try:
    from tf_keras.layers import DepthwiseConv2D as OriginalDepthwiseConv2D
except ImportError:
    from tensorflow.keras.layers import DepthwiseConv2D as OriginalDepthwiseConv2D

class CustomDepthwiseConv2D(OriginalDepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)
        super(CustomDepthwiseConv2D, self).__init__(*args, **kwargs)

custom_objects = {'DepthwiseConv2D': CustomDepthwiseConv2D}

# --- Model Configurations ---
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
MODEL_44_PATH = os.path.join(MODEL_DIR, "efficientnetv2-s-BTI44impact-97.62.h5")
# The user might have renamed the file in the repo. Let's check the filename again.
# In the old version it was "efficientnetv2-s-BTI44impact-97.62.h5".
# I'll use a dynamic check.

MODEL_17_PATH = os.path.join(MODEL_DIR, "brain_tumor_convnext_tiny_scripted.pt")

CLASS_LABELS_44 = [
    'Astrocitoma T1', 'Astrocitoma T1C+', 'Astrocitoma T2',
    'Carcinoma T1', 'Carcinoma T1C+', 'Carcinoma T2',
    'Ependimoma T1', 'Ependimoma T1C+', 'Ependimoma T2',
    'Ganglioglioma T1', 'Ganglioglioma T1C+', 'Ganglioglioma T2',
    'Germinoma T1', 'Germinoma T1C+', 'Germinoma T2',
    'Glioblastoma T1', 'Glioblastoma T1C+', 'Glioblastoma T2',
    'Granuloma T1', 'Granuloma T1C+', 'Granuloma T2',
    'Meduloblastoma T1', 'Meduloblastoma T1C+', 'Meduloblastoma T2',
    'Meningioma T1', 'Meningioma T1C+', 'Meningioma T2',
    'Neurocitoma T1', 'Neurocitoma T1C+', 'Neurocitoma T2',
    'Oligodendroglioma T1', 'Oligodendroglioma T1C+', 'Oligodendroglioma T2',
    'Papiloma T1', 'Papiloma T1C+', 'Papiloma T2',
    'Schwannoma T1', 'Schwannoma T1C+', 'Schwannoma T2',
    'Tuberculoma T1', 'Tuberculoma T1C+', 'Tuberculoma T2',
    '_NORMAL T1', '_NORMAL T2'
]

# Full 17 Labels (As per stable v2.0)
CLASS_LABELS_17 = [
    'Glioma (Astrocitoma, Ganglioglioma, Glioblastoma, Oligodendroglioma, Ependimoma) T1',
    'Glioma (Astrocitoma, Ganglioglioma, Glioblastoma, Oligodendroglioma, Ependimoma) T1C+',
    'Glioma (Astrocitoma, Ganglioglioma, Glioblastoma, Oligodendroglioma, Ependimoma) T2',
    'Meningioma (Low Grade, Atypical, Anaplastic, Transitional) T1',
    'Meningioma (Low Grade, Atypical, Anaplastic, Transitional) T1C+',
    'Meningioma (Low Grade, Atypical, Anaplastic, Transitional) T2',
    'NORMAL T1',
    'NORMAL T2',
    'Neurocitoma (Central - Intraventricular, Extraventricular) T1',
    'Neurocitoma (Central - Intraventricular, Extraventricular) T1C+',
    'Neurocitoma (Central - Intraventricular, Extraventricular) T2',
    'Other Types of Injuries (Abscesses, Cysts, Miscellaneous Encephalopathies) T1',
    'Other Types of Injuries (Abscesses, Cysts, Miscellaneous Encephalopathies) T1C+',
    'Other Types of Injuries (Abscesses, Cysts, Miscellaneous Encephalopathies) T2',
    'Schwannoma (Acoustic, Vestibular - Trigeminal) T1',
    'Schwannoma (Acoustic, Vestibular - Trigeminal) T1C+',
    'Schwannoma (Acoustic, Vestibular - Trigeminal) T2'
]

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
    """Load both diagnostic models."""
    global model_44, model_17
    
    if os.path.exists(MODEL_DIR):
        files = os.listdir(MODEL_DIR)
        
        # Load 44-class (TensorFlow)
        h5_files = [f for f in files if f.endswith('.h5') and not f.startswith('.')]
        if h5_files:
            path_44 = os.path.join(MODEL_DIR, h5_files[0])
            try:
                # Use compile=False to avoid issues, but we'll compile with original settings
                import tf_keras
                model_44 = tf_keras.models.load_model(path_44, custom_objects=custom_objects, compile=False)
                model_44.compile(optimizer='Adamax', loss='categorical_crossentropy')
                print(f"Loaded 44-class model: {path_44}")
            except Exception as e:
                print(f"Error loading 44-class model: {e}")

        # Load 17-class (PyTorch)
        pt_files = [f for f in files if f.endswith('.pt') and not f.startswith('.')]
        if pt_files:
            path_17 = os.path.join(MODEL_DIR, pt_files[0])
            try:
                model_17 = torch.jit.load(path_17, map_location="cpu")
                model_17.eval()
                print(f"Loaded 17-class model: {path_17}")
            except Exception as e:
                print(f"Error loading 17-class model: {e}")

@gpu_decorator
def verify_with_medgemma(image_bytes: io.BytesIO, prediction_results: str) -> dict:
    """
    Runs MedGemma 1.5 4B for clinical verification using HF ZeroGPU.
    """
    global medgemma_processor, medgemma_model
    from transformers import AutoProcessor, AutoModelForImageTextToText, BitsAndBytesConfig
    import torch
    from PIL import Image

    model_id = "google/medgemma-1.5-4b-it"
    hf_token = os.getenv("HF_TOKEN")
    
    try:
        if medgemma_processor is None:
            medgemma_processor = AutoProcessor.from_pretrained(model_id, token=hf_token)

        if medgemma_model is None:
            # Use BitsAndBytesConfig for robust 4-bit loading
            quant_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.bfloat16
            )
            medgemma_model = AutoModelForImageTextToText.from_pretrained(
                model_id,
                torch_dtype=torch.bfloat16,
                device_map="auto",
                quantization_config=quant_config,
                token=hf_token
            )

        image_bytes.seek(0)
        image = Image.open(image_bytes).convert("RGB")
        prompt = (
            f"System: You are a senior neuroradiologist. Analyze this brain MRI.\n"
            f"User: The AI classifier suggests: {prediction_results}. "
            f"Provide a 1-sentence final diagnosis and a brief radiological explanation."
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
        return {"verified_answer": "Verification Unavailable", "explanation": f"MedGemma error: {str(e)}"}

def predict_tumor(image_bytes: io.BytesIO, model_type: str = "44BTIS", run_verification: bool = False) -> dict:
    """Main prediction pipeline."""
    try:
        image_bytes.seek(0)
        img = Image.open(image_bytes).convert('RGB')
        
        if model_type == "44BTIS":
            if model_44 is None: return {"error": "44-class model not loaded."}
            img_res = img.resize((224, 224))
            img_array = np.array(img_res)
            img_array = np.expand_dims(img_array, axis=0)
            
            # EfficientNetV2 prediction
            preds = model_44.predict(img_array)[0]
            labels = CLASS_LABELS_44
        else:
            # ConVext prediction (DON'T TOUCH)
            if model_17 is None: return {"error": "17-class model not loaded."}
            preprocess = T.Compose([
                T.Resize((224, 224)),
                T.ToTensor(),
                T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
            ])
            input_tensor = preprocess(img).unsqueeze(0)
            with torch.no_grad():
                outputs = model_17(input_tensor)
                preds = torch.softmax(outputs, dim=1)[0].numpy()
            labels = CLASS_LABELS_17

        top_3_idx = np.argsort(preds)[::-1][:3]
        predictions = [
            {"label": labels[idx], "confidence": round(float(preds[idx]) * 100, 2)} 
            for idx in top_3_idx
        ]

        results = {"model_type": model_type, "predictions": predictions}

        if run_verification:
            pred_str = ", ".join([f"{p['label']} ({p['confidence']}%)" for p in predictions])
            image_bytes.seek(0)
            results["medgemma_verification"] = verify_with_medgemma(image_bytes, pred_str)

        return results
    except Exception as e:
        return {"error": f"Internal logic error: {str(e)}"}
