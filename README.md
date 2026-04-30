
# <img src="frontend/public/TumorVisionLOGO-removebg.png" width="48" height="48" valign="middle"> TumorVision


[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![FastAPI](https://img.shields.io/badge/backend-FastAPI-009688.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/frontend-React-61DAFB.svg?style=flat&logo=react&logoColor=black)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/build-Vite-646CFF.svg?style=flat&logo=vite&logoColor=white)](https://vitejs.dev/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-D00000?style=flat&logo=keras&logoColor=white)](https://keras.io/)
[![Kaggle Dataset](https://img.shields.io/badge/Kaggle-Dataset-20BEFF?style=flat&logo=Kaggle&logoColor=white)](https://www.kaggle.com/datasets/fernando2rad/brain-tumor-mri-images-44c)

<div align="center">
  <br/>
  <a href="https://huggingface.co/spaces/mingnatthakitt/TumorVision">
    <img src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-xl-dark.svg" alt="Try our demo in Hugging Face Spaces" width="300px">
  </a>
  <br/>
  <br/>
</div>

**Pioneering AI-Powered Brain Tumor Diagnostics.**

TumorVision is a medical diagnostic platform designed to support healthcare professionals in identifying brain tumors from MRI scans. By combining advanced machine learning with a premium, user-centric interface, TumorVision provides rapid, accurate, and actionable insights.

|<img width="70%" alt="image" src="https://github.com/user-attachments/assets/57f8d5be-e2da-462b-b4ca-e97bbe995066" />|
| :---: |
---

## ✨ Key Features

### 🔬 Advanced AI Classification
- **EfficientNetV2-S Backbone**: Leverages a state-of-the-art **EfficientNetV2** architecture, optimized for both parameter efficiency and training speed.
- **44-Class Granularity**: Trained to recognize 44 distinct tumor signatures, providing one of the most granular open-source classification models for brain MRIs.
- **Top-3 Prediction Engine**: Provides a ranked list of potential tumor types with real-time probability bars, ensuring clinicians have a comprehensive view of diagnostic possibilities.
- **Robust Training Pipeline**:
    - **Dataset**: ~16,000+ MRI slices across 44 categories.
    - **Optimization**: Adam optimizer with categorical cross-entropy.
    - **Validation**: 96.69% average accuracy achieved via 5-fold cross-validation.
- **Legacy Keras Support**: Custom compatibility layer for high-fidelity model loading of `.h5` weights in modern TensorFlow environments.

<p align="center">
  <img src="docs/training/mri_samples.png" width="600" alt="MRI Samples" />
</p>

- **Dataset** from kaggle: https://www.kaggle.com/datasets/fernando2rad/brain-tumor-mri-images-44c

### 🎨 Premium User Experience
- **Futuristic Glassmorphism UI**: A stunning, dark-themed interface built with vanilla CSS for maximum performance and visual excellence.
- **Interactive MRI Upload**: Advanced drag-and-drop zone with instant image preview and animated analysis states.
- **Fluid Animations**: Smooth transitions and layout animations powered by **Framer Motion** for a professional, high-end feel.
- **Fully Responsive**: Optimized for desktops, tablets, and mobile devices.

### ⚙️ Model Architecture & Performance
The TumorVision model follows a deep transfer learning approach with a custom classification head.

#### Architecture Overview
The model takes a `224x224x3` MRI input, passes it through the EfficientNetV2-S feature extractor, and terminates in a series of dense layers with batch normalization and dropout for regularization.

<p align="center">
  <img src="docs/training/model_architecture.png" width="450" alt="Model Architecture" />
</p>

#### Performance Metrics & Technical Evaluation
The model was rigorously evaluated across 44 distinct classes using a test set of 1,232 images. The high scores across all metrics demonstrate the model's reliability for clinical screening support.

| Metric | Score | Description |
| :--- | :--- | :--- |
| **Accuracy** | **96.69%** | Overall correctness across all 44 tumor categories. |
| **Precision** | **98.0%** | Reliability of positive predictions (minimizing False Positives). |
| **Recall** | **97.0%** | Sensitivity to tumor detection (minimizing False Negatives). |
| **F1-Score** | **97.0%** | Harmonic mean of Precision and Recall, reflecting overall robustness. |

<p align="center">
  <img src="docs/training/kfold_results.png" width="55%" />
  <img src="docs/training/confusion_matrix.png" width="40%" />
</p>

<br/>

<details>
<summary>📊 Click to view Detailed Classification Report (44 Classes)</summary>

<br/>

```text
precision    recall  f1-score   support

        Astrocitoma T1       1.00      1.00      1.00        28
      Astrocitoma T1C+       1.00      0.96      0.98        28
        Astrocitoma T2       0.93      0.96      0.95        28
          Carcinoma T1       1.00      1.00      1.00        28
        Carcinoma T1C+       1.00      0.93      0.96        28
          Carcinoma T2       1.00      1.00      1.00        28
         Ependimoma T1       1.00      0.75      0.86        28
       Ependimoma T1C+       1.00      1.00      1.00        28
         Ependimoma T2       1.00      0.43      0.60        28
      Ganglioglioma T1       1.00      1.00      1.00        28
    Ganglioglioma T1C+       1.00      1.00      1.00        28
      Ganglioglioma T2       1.00      1.00      1.00        28
          Germinoma T1       1.00      1.00      1.00        28
        Germinoma T1C+       1.00      1.00      1.00        28
          Germinoma T2       1.00      1.00      1.00        28
       Glioblastoma T1       1.00      1.00      1.00        28
     Glioblastoma T1C+       1.00      1.00      1.00        28
       Glioblastoma T2       1.00      1.00      1.00        28
          Granuloma T1       1.00      1.00      1.00        28
        Granuloma T1C+       1.00      1.00      1.00        28
          Granuloma T2       1.00      1.00      1.00        28
     Meduloblastoma T1       1.00      1.00      1.00        28
   Meduloblastoma T1C+       1.00      1.00      1.00        28
     Meduloblastoma T2       0.64      1.00      0.78        28
         Meningioma T1       0.93      1.00      0.97        28
       Meningioma T1C+       0.93      0.89      0.91        28
         Meningioma T2       1.00      0.86      0.92        28
        Neurocitoma T1       1.00      1.00      1.00        28
      Neurocitoma T1C+       0.97      1.00      0.98        28
        Neurocitoma T2       1.00      1.00      1.00        28
  Oligodendroglioma T1       1.00      1.00      1.00        28
Oligodendroglioma T1C+       1.00      1.00      1.00        28
  Oligodendroglioma T2       1.00      0.82      0.90        28
           Papiloma T1       1.00      1.00      1.00        28
         Papiloma T1C+       1.00      1.00      1.00        28
           Papiloma T2       1.00      1.00      1.00        28
         Schwannoma T1       0.80      1.00      0.89        28
       Schwannoma T1C+       0.97      1.00      0.98        28
         Schwannoma T2       1.00      1.00      1.00        28
        Tuberculoma T1       1.00      1.00      1.00        28
      Tuberculoma T1C+       1.00      1.00      1.00        28
        Tuberculoma T2       1.00      1.00      1.00        28
            _NORMAL T1       1.00      1.00      1.00        28
            _NORMAL T2       0.78      1.00      0.88        28

              accuracy                           0.97      1232
             macro avg       0.98      0.97      0.97      1232
          weighted avg       0.98      0.97      0.97      1232
```
</details>

<br/>

### 📚 Medical Intelligence Database
- **Searchable Encyclopedia**: A dedicated section covering 14 major brain tumor categories (including Astrocytoma, Glioblastoma, Meningioma, and more).
- **Reference Library**: Over 40+ reference MRI images integrated to help users compare and learn about different tumor pathologies.

### 🛠️ Unified Architecture
- **Decoupled Modern Stack**: Built with **React (Vite)**, **TypeScript**, and **FastAPI**.
- **Unified Deployment**: Optimized for **Hugging Face Spaces** as a Docker-based deployment where the FastAPI backend serves the production-built React frontend.

---

## 🛠️ Technical Stack

- **Frontend**: React 18, TypeScript, Vite, Framer Motion, Lucide Icons.
- **Backend**: FastAPI (Python), TensorFlow/Keras, Uvicorn.
- **DevOps**: Docker, Git LFS, Makefile.

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v20+)
- Python (3.10.x)
- Conda (recommended)

### Local Setup
1. **Initialize Git LFS**:
   ```bash
   git lfs pull
   ```
2. **Install Dependencies**:
   ```bash
   make install
   ```
3. **Run Development Server**:
   ```bash
   make dev
   ```
   *The app will be available at `http://localhost:5173`.*

---

## ☁️ Deployment

This project is deployed on **Hugging Face Spaces** using Docker.

1. **Prerequisites**: Ensure Git LFS is installed and tracking the model file.
2. **Setup Space**: Create a new Docker Space on Hugging Face.
3. **Push Code**: Push the repository (including the model file) to the Hugging Face remote.
4. **Automatic Build**: Hugging Face will automatically build the Docker image and deploy the application.

---

## ⚖️ Disclaimer
*This tool is intended for research and educational purposes to assist medical professionals. It should not be used as a standalone diagnostic tool for clinical decision-making.*
