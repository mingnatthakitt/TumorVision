
# <img src="frontend/public/TumorVisionLOGO-removebg.png" width="48" height="48" valign="middle"> TumorVision


[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![FastAPI](https://img.shields.io/badge/backend-FastAPI-009688.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/frontend-React-61DAFB.svg?style=flat&logo=react&logoColor=black)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/build-Vite-646CFF.svg?style=flat&logo=vite&logoColor=white)](https://vitejs.dev/)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/mingnatthakitt/TumorVision)

<div align="center">
  <a href="https://huggingface.co/spaces/mingnatthakitt/TumorVision">
    <img src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-xl-dark.svg" alt="Try our demo in Hugging Face Spaces">
  </a>
</div>

**Pioneering AI-Powered Brain Tumor Diagnostics.**

TumorVision is a state-of-the-art medical diagnostic platform designed to support healthcare professionals in identifying brain tumors from MRI scans. By combining advanced machine learning with a premium, user-centric interface, TumorVision provides rapid, accurate, and actionable insights.

---

## ✨ Key Features

### 🔬 Advanced AI Classification
- **44-Class Model**: Leverages an **EfficientNetV2** deep learning architecture trained to recognize 44 distinct tumor signatures.
- **Top-3 Prediction Engine**: Provides a ranked list of potential tumor types with real-time probability bars, ensuring clinicians have a comprehensive view of diagnostic possibilities.
- **Legacy Keras Support**: Optimized for high-fidelity model loading and execution using specialized compatibility layers.

### 🎨 Premium User Experience
- **Futuristic Glassmorphism UI**: A stunning, dark-themed interface built with vanilla CSS for maximum performance and visual excellence.
- **Interactive MRI Upload**: Advanced drag-and-drop zone with instant image preview and animated analysis states.
- **Fluid Animations**: Smooth transitions and layout animations powered by **Framer Motion** for a professional, high-end feel.
- **Fully Responsive**: Optimized for desktops, tablets, and mobile devices.

### 📚 Medical Intelligence Database
- **Searchable Encyclopedia**: A dedicated section covering 14 major brain tumor categories (including Astrocytoma, Glioblastoma, Meningioma, and more).
- **Reference Library**: Over 40+ reference MRI images integrated to help users compare and learn about different tumor pathologies.

### ⚙️ Unified Architecture
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
