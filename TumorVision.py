import streamlit as st
import numpy as np
from PIL import Image
#Model Pipeline
#import modelpipeline

# Backend functions and libraries
import os
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
from tensorflow.keras.layers import DepthwiseConv2D as OriginalDepthwiseConv2D

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

# Real Page - Streamlit interface
def show():
    
    st.write("#")

    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        st.write("")

    with col2:
        st.markdown("<h1 style='text-align: left; font:sans-serif; font-size: 40px; font-weight:bold; color:#3c6ca8;'>TumorVision <span style= color:black; >- Try our AI that identifies brain tumor types</span></h1>", unsafe_allow_html=True)
        #st.write("Upload an MRI image of a brain to identify its tumor type.")
        with st.container(border=True):
            uploaded_file = st.file_uploader("Upload an MRI image of a brain to identify its tumor type.", type=["jpg", "png", "jpeg"])
            if uploaded_file is not None:
                st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
                image = Image.open(uploaded_file).convert('RGB')
                image = image.resize((224, 224))  # Resize to match the model's input size
                img_array = np.array(image)
                img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

                st.write("Identifying...")
                prediction1, prediction2, prediction3 = predict_and_display(img_array)

                st.write(f"Prediction with Most Probability: {prediction1}")
                st.write(f"Prediction with Second Most Probability: {prediction2}")
                st.write(f"Prediction with Third Most Probability: {prediction3}")
    
    with col3:
        st.write("")
# Display the interface
if __name__ == "__main__":
    show()
