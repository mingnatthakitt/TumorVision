# TumorVision

TumorVision is an AI-powered medical diagnostic tool built to assist healthcare professionals in identifying brain tumors from MRI scans. It uses an EfficientNetV2 model to classify tumors into 44 different categories with high accuracy.

## Architecture

This project was recently reworked from a Streamlit monolith into a modern, decoupled stack:

- **Frontend:** React (Vite), TypeScript, Framer Motion, Vanilla CSS (Glassmorphism design)
- **Backend:** FastAPI, TensorFlow/Keras, Python 3.10+

## Local Development

We've provided a simple `Makefile` to handle all development tasks.

### Prerequisites
- Node.js (v20+)
- Conda (Miniconda/Anaconda)
- Git LFS

### 1. Setup Environment

First, ensure you have pulled the actual model files using Git LFS:
```bash
git lfs install
git lfs pull
```

Ensure your `efficientnetv2-s-BTI44impact-97.62.h5` model is placed in the `backend/models/` directory.

Then, install all dependencies:
```bash
make install
```
*(This will install frontend npm packages and use `conda run` to install backend pip packages in the `tumorvision` environment).*

### 2. Run the App

Start both the FastAPI backend and the Vite frontend simultaneously:
```bash
make dev
```
- Frontend will be available at `http://localhost:5173`
- Backend API will be available at `http://localhost:8000`
- API Documentation at `http://localhost:8000/docs`

## Deployment

The app is configured to be deployed easily on **Render.com** using the provided `render.yaml` Blueprint.

1. Connect your GitHub repository to Render
2. Render will automatically detect the `render.yaml` file
3. Two services will be created: `tumorvision-api` and `tumorvision-frontend`
4. The frontend will automatically link to the backend via the `VITE_API_URL` environment variable.

### Note on Keras Compatibility
The backend forces `TF_USE_LEGACY_KERAS=1` to ensure compatibility between newer TensorFlow versions (2.16+) and the older `.h5` model format.
