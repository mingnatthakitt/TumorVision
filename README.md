# <img src="frontend/public/TumorVisionLOGO-removebg.png" width="48" height="48" valign="middle"> TumorVision

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![FastAPI](https://img.shields.io/badge/backend-FastAPI-009688.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/frontend-React-61DAFB.svg?style=flat&logo=react&logoColor=black)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/build-Vite-646CFF.svg?style=flat&logo=vite&logoColor=white)](https://vitejs.dev/)
[![Render](https://img.shields.io/badge/deploy-Render-46E3B7.svg?style=flat&logo=render&logoColor=white)](https://render.com/)

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
- **Unified Deployment**: Specially configured for **Render.com** as a single-service deployment where the FastAPI backend serves the production-built React frontend.

---

## 🛠️ Technical Stack

- **Frontend**: React 18, TypeScript, Vite, Framer Motion, Lucide Icons.
- **Backend**: FastAPI (Python), TensorFlow/Keras, Uvicorn.
- **DevOps**: Makefile, Git LFS, Render Blueprint (`render.yaml`).

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

This project is optimized for **Render.com**.

1. Connect your repository to Render.
2. Create a new **Web Service**.
3. Render will automatically detect the `render.yaml` configuration and deploy your unified app.

---

## ⚖️ Disclaimer
*This tool is intended for research and educational purposes to assist medical professionals. It should not be used as a standalone diagnostic tool for clinical decision-making.*
