import streamlit as st
import numpy as np
from PIL import Image
#Model Pipeline
import modelpipeline

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
                prediction1, prediction2, prediction3 = modelpipeline.predict_and_display(img_array)

                st.write(f"Prediction with Most Probability: {prediction1}")
                st.write(f"Prediction with Second Most Probability: {prediction2}")
                st.write(f"Prediction with Third Most Probability: {prediction3}")
    
    with col3:
        st.write("")
# Display the interface
if __name__ == "__main__":
    show()
