# Backend functions and libraries — ported from modelpipeline.py
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import DepthwiseConv2D as OriginalDepthwiseConv2D
from PIL import Image

# Ensure TensorFlow uses CPU
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# Force legacy Keras for compatibility with older .h5 models
os.environ["TF_USE_LEGACY_KERAS"] = "1"

# Custom layer handling
class CustomDepthwiseConv2D(OriginalDepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)  # Remove the 'groups' parameter if present
        super(CustomDepthwiseConv2D, self).__init__(*args, **kwargs)

custom_objects = {'DepthwiseConv2D': CustomDepthwiseConv2D}

# Model state
model = None

# Model path — resolve relative to this file
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
MODEL_FILENAME = "efficientnetv2-s-BTI44impact-97.62.h5"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILENAME)

# Class labels for predictions (44 classes — BTI44impact model)
CLASS_LABELS = [
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


def load_tumor_model():
    """Load the EfficientNetV2 model at startup."""
    global model

    if not os.path.exists(MODEL_PATH):
        print(f"Warning: Model file not found at {MODEL_PATH}")
        print(f"Please place '{MODEL_FILENAME}' in the '{MODEL_DIR}' directory.")
        return

    file_size = os.path.getsize(MODEL_PATH)
    if file_size < 1024:
        print(f"Warning: Model file appears to be a Git LFS pointer ({file_size} bytes).")
        print("Run 'git lfs pull' to download the actual model data.")
        return

    try:
        model = tf.keras.models.load_model(
            MODEL_PATH,
            custom_objects=custom_objects,
            compile=False
        )
        model.compile(optimizer='Adamax', loss='categorical_crossentropy')
        print(f"Model loaded successfully from {MODEL_PATH}")
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None


def predict_tumor(image_bytes: bytes) -> dict:
    """
    Predict tumor type from image bytes.
    Returns top-3 predictions with probabilities.
    """
    if model is None:
        return {"error": "Model not loaded. Check server logs."}

    # Preprocess — same pipeline as original TumorVision.py
    img = Image.open(image_bytes).convert('RGB')
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict
    preds = model.predict(img_array)
    probabilities = preds[0]
    top_3_indices = np.argsort(probabilities)[::-1][:3]
    top_3_probabilities = probabilities[top_3_indices] * 100

    predictions = []
    for i, idx in enumerate(top_3_indices):
        predictions.append({
            "rank": i + 1,
            "label": CLASS_LABELS[idx],
            "probability": round(float(top_3_probabilities[i]), 2)
        })

    return {"predictions": predictions}
