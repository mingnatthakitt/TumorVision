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

# Load environment variables (HF_TOKEN, etc.)
load_dotenv()

# Import DepthwiseConv2D from the correct Keras backend
try:
    from tf_keras.layers import DepthwiseConv2D as OriginalDepthwiseConv2D
except ImportError:
    from tensorflow.keras.layers import DepthwiseConv2D as OriginalDepthwiseConv2D

# Custom layer handling
class CustomDepthwiseConv2D(OriginalDepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)  # Remove the 'groups' parameter if present
        super(CustomDepthwiseConv2D, self).__init__(*args, **kwargs)

custom_objects = {'DepthwiseConv2D': CustomDepthwiseConv2D}

# Model states
model_44 = None
model_17 = None

# HF Configuration for MedGemma
HF_TOKEN = os.getenv("HF_TOKEN")
MEDGEMMA_MODEL_ID = "google/medgemma-1.5-4b-it" 
# but let's use a reliable VLM endpoint if the specific one is restricted.
# We will use the provided token.

# Model paths
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
MODEL_44_FILENAME = "efficientnetv2-s-BTI44impact-97.62.h5"
MODEL_17_FILENAME = "brain_tumor_convnext_tiny_scripted.pt"

MODEL_44_PATH = os.path.join(MODEL_DIR, MODEL_44_FILENAME)
MODEL_17_PATH = os.path.join(MODEL_DIR, MODEL_17_FILENAME)

# Class labels for 44-class model (BTIS)
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

# Class labels for 17-class model (ConVext)
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


def load_tumor_model():
    """Load both ML models at startup."""
    global model_44, model_17

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


def verify_with_medgemma(image_bytes: bytes, initial_prediction: str, confidence: float) -> str:
    """
    Use MedGemma 1.5 4B via HF Inference API to verify the prediction.
    """
    if not HF_TOKEN:
        return "Verification unavailable (HF_TOKEN missing)."

    # Standard VLM Prompt for Medical Verification
    prompt = (
        f"Analyze this brain MRI image. The classifier suggested '{initial_prediction}' "
        f"with {confidence}% confidence. As a medical imaging expert, provide a single final answer "
        f"stating the most probable tumor type and a brief explanation of the radiological signs "
        f"supporting this diagnosis."
    )

    # API Endpoint (using google/paligemma-3b-mix-224 as a baseline if specific 1.5 4B is restricted)
    # The user mentioned MedGemma 1.5 4B specifically.
    API_URL = f"https://api-inference.huggingface.co/models/{MEDGEMMA_MODEL_ID}"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}

    try:
        # Encode image to base64
        image_b64 = base64.b64encode(image_bytes).decode("utf-8")
        
        payload = {
            "inputs": {
                "image": image_b64,
                "text": prompt
            },
            "parameters": {"max_new_tokens": 150}
        }

        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get("generated_text", "No response from model.")
            return str(result)
        else:
            return f"Verification failed (Status {response.status_code}): {response.text}"
    except Exception as e:
        return f"Verification error: {str(e)}"


def predict_tumor(image_bytes: io.BytesIO, model_type: str = "44BTIS") -> dict:
    """
    Predict tumor type using selected model.
    """
    # Rewind buffer
    image_bytes.seek(0)
    raw_bytes = image_bytes.read()
    image_bytes.seek(0)

    if model_type == "44BTIS":
        if model_44 is None:
            return {"error": "44-class model not loaded."}
        
        img = Image.open(image_bytes).convert('RGB')
        img = img.resize((224, 224))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        
        preds = model_44.predict(img_array)
        probs = preds[0]
        labels = CLASS_LABELS_44
    else:
        if model_17 is None:
            return {"error": "17-class model not loaded."}
        
        # PyTorch Preprocessing
        img = Image.open(image_bytes).convert('RGB')
        preprocess = T.Compose([
            T.Resize((224, 224)),
            T.ToTensor(),
            T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        input_tensor = preprocess(img).unsqueeze(0)
        
        with torch.no_grad():
            outputs = model_17(input_tensor)
            probs = torch.softmax(outputs, dim=1)[0].numpy()
        labels = CLASS_LABELS_17

    top_3_indices = np.argsort(probs)[::-1][:3]
    predictions = []
    for i, idx in enumerate(top_3_indices):
        predictions.append({
            "rank": i + 1,
            "label": labels[idx],
            "probability": round(float(probs[idx] * 100), 2)
        })

    # MedGemma Verification
    primary_pred = predictions[0]["label"]
    primary_conf = predictions[0]["probability"]
    
    verification = verify_with_medgemma(raw_bytes, primary_pred, primary_conf)

    return {
        "predictions": predictions,
        "verification": verification,
        "model_used": model_type
    }
