# Backend functions and libraries
import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
from tensorflow.keras.layers import DepthwiseConv2D as OriginalDepthwiseConv2D
from PIL import Image

# Ensure TensorFlow uses CPU
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Custom layer handling
class CustomDepthwiseConv2D(OriginalDepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)  # Remove the 'groups' parameter if present
        super(CustomDepthwiseConv2D, self).__init__(*args, **kwargs)

custom_objects = {'DepthwiseConv2D': CustomDepthwiseConv2D}

# Load the model with custom objects
model = tf.keras.models.load_model(
    'efficientnetv2-s-BTI44impact-97.62.h5', 
    custom_objects=custom_objects
)
model.compile(optimizer='Adamax', loss='categorical_crossentropy')  # Adjust the optimizer and loss as per your requirements

# Class labels for predictions
class_labels = [
    'Astrocitoma T1', 'Astrocitoma T1C+', 'Astrocitoma T2', 'Carcinoma T1', 'Carcinoma T1C+', 'Carcinoma T2',
    'Ependimoma T1', 'Ependimoma T1C+', 'Ependimoma T2', 'Ganglioglioma T1', 'Ganglioglioma T1C+', 'Ganglioglioma T2',
    'Germinoma T1', 'Germinoma T1C+', 'Germinoma T2', 'Glioblastoma T1', 'Glioblastoma T1C+', 'Glioblastoma T2',
    'Granuloma T1', 'Granuloma T1C+', 'Granuloma T2', 'Meduloblastoma T1', 'Meduloblastoma T1C+', 'Meduloblastoma T2',
    'Meningioma T1', 'Meningioma T1C+', 'Meningioma T2', 'Neurocitoma T1', 'Neurocitoma T1C+', 'Neurocitoma T2',
    'Oligodendroglioma T1', 'Oligodendroglioma T1C+', 'Oligodendroglioma T2', 'Papiloma T1', 'Papiloma T1C+', 'Papiloma T2',
    'Schwannoma T1', 'Schwannoma T1C+', 'Schwannoma T2', 'Tuberculoma T1', 'Tuberculoma T1C+', 'Tuberculoma T2',
    '_NORMAL T1', '_NORMAL T2'
]

# Function to predict and display results
def predict_and_display(img_array):
    preds = model.predict(img_array)
    probabilities = preds[0]
    top_3_indices = np.argsort(probabilities)[::-1][:3]
    top_3_probabilities = probabilities[top_3_indices] * 100

    prediction1 = f"{class_labels[top_3_indices[0]]} : Probability {top_3_probabilities[0]:.2f}%"
    prediction2 = f"{class_labels[top_3_indices[1]]} : Probability {top_3_probabilities[1]:.2f}%"
    prediction3 = f"{class_labels[top_3_indices[2]]} : Probability {top_3_probabilities[2]:.2f}%"
    return prediction1, prediction2, prediction3
