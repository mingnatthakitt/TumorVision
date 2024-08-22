import streamlit as st
import numpy as np
from PIL import Image


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
    'efficientnetv2-s-BTI15-97.91.h5', 
    custom_objects=custom_objects
)
model.compile(optimizer='Adamax', loss='categorical_crossentropy')  # Adjust the optimizer and loss as per your requirements

# Class labels for predictions
class_labels = ['Astrocitoma', 'Carcinoma', 'Ependimoma', 'Ganglioglioma', 'Germinoma', 'Glioblastoma', 'Granuloma', 'Meduloblastoma', 'Meningioma', 'Neurocitoma', 'Oligodendroglioma', 'Papiloma', 'Schwannoma', 'Tuberculoma', '_NORMAL']

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
        st.markdown("<p style='text-align: left; font:sans-serif; font-size: 40px; font-weight:bold; color:#3c6ca8;'>TumorVision <span style= color:black; >- Try our AI that identifies brain tumor types</span></p>", unsafe_allow_html=True)
        #Usage
        st.markdown("<p style='text-align: left; font:sans-serif; font-size: 27px; font-weight:bold;'>Steps to utilize our services</p>", unsafe_allow_html=True)
        st.write("""
                - Step 1 : Upload the image, You can either drag and drop or browse through the files.
                - Step 2 : Wait a few moments for the model to analyse.
                - Step 3 : The model will output 3 results ranking from probabilities, and you're done.
            """)





        with st.container(border=True):
            uploaded_file = st.file_uploader("Upload an MRI image of a brain to identify its tumor type.", type=["jpg", "png", "jpeg"])
            if uploaded_file is not None:
                col4, col5, col6 = st.columns([0.25, 0.5, 0.25])
                with col5:
                    with st.spinner('Analyzing...'):
                        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
                        image = Image.open(uploaded_file).convert('RGB')
                        image = image.resize((224, 224))  # Resize to match the model's input size
                        img_array = np.array(image)
                        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

                    #st.write("Identifying...")
                        prediction1, prediction2, prediction3 = predict_and_display(img_array)

                        st.write(f"Prediction with Most Probability: :blue-background[{prediction1}]")
                        st.write(f"Prediction with Second Most Probability: :green-background[{prediction2}]")
                        st.write(f"Prediction with Third Most Probability: :orange-background[{prediction3}]")
            else:
                st.write("Waiting on MRI image upload")
    
    with col3:
        st.write("")
# Display the interface
if __name__ == "__main__":
    show()
