
# <img src="frontend/public/TumorVisionLOGO-removebg.png" width="48" height="48" valign="middle"> TumorVision


[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![FastAPI](https://img.shields.io/badge/backend-FastAPI-009688.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/frontend-React-61DAFB.svg?style=flat&logo=react&logoColor=black)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/build-Vite-646CFF.svg?style=flat&logo=vite&logoColor=white)](https://vitejs.dev/)
![Docker](https://img.shields.io/badge/container-Docker-2496ED?style=flat&logo=docker&logoColor=white)
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

<p align="center">
  <img src="https://github.com/user-attachments/assets/57f8d5be-e2da-462b-b4ca-e97bbe995066" width="70%" />
</p>

---

## ✨ Key Features

### 🔬 Advanced AI Classification
- **EfficientNetV2-S (BTIS 44)**: Leverages a state-of-the-art **EfficientNetV2** architecture, optimized for 44 granular tumor categories.
- **ConVext-Tiny (17-Class)**: A newer, highly stable model using the **ConvNeXt-Tiny** architecture. It provides superior generalization and stability by grouping major tumor families.
- **MedGemma 1.5 4B Verification**: A "Medical Diagnostic Peer-Review" layer. Every prediction is verified by a Vision-Language Model (VLM) specialized in radiology to provide a final explanation and confirmed diagnosis.
- **Top-3 Prediction Engine**: Provides a ranked list of potential tumor types with real-time probability bars.

<br/>

<details>
<summary>📑 View Technical Documentation: ConVext-Tiny (17-Class Model)</summary>

<br/>

#### Performance Metrics
- **Final Accuracy: 98.0%**
- **Test Stability: 93.71% (+/- 5.58)**

| Metric | Score | Description |
| :--- | :--- | :--- |
| **Accuracy** | **98.0%** | Overall correctness on the 17-class test set. |
| **Precision** | **98.0%** | Reliability of positive predictions. |
| **Recall** | **97.0%** | Sensitivity to tumor detection. |
| **F1-Score** | **97.0%** | Robustness across all 17 categories. |

#### Model Architecture Overview
The **ConvNeXt-Tiny** architecture is a modern pure-convolutional network that competes with Vision Transformers in performance while maintaining the efficiency and simplicity of standard convolutions.

<details>
<summary>💻 View Layer-by-Layer Architecture Summary</summary>

<br/>

```text
===============================================================================================
Layer (type:depth-idx)                        Output Shape              Param #
===============================================================================================
ConvNeXt                                      [1, 17]                   --
├─Sequential: 1-1                             [1, 768, 7, 7]            --
│    └─Conv2dNormActivation: 2-1              [1, 96, 56, 56]           --
│    │    └─Conv2d: 3-1                       [1, 96, 56, 56]           4,704
│    │    └─LayerNorm2d: 3-2                  [1, 96, 56, 56]           192
│    └─Sequential: 2-2                        [1, 96, 56, 56]           --
│    │    └─CNBlock: 3-3                      [1, 96, 56, 56]           79,296
│    │    └─CNBlock: 3-4                      [1, 96, 56, 56]           79,296
│    │    └─CNBlock: 3-5                      [1, 96, 56, 56]           79,296
│    └─Sequential: 2-3                        [1, 192, 28, 28]          --
│    │    └─LayerNorm2d: 3-6                  [1, 96, 56, 56]           192
│    │    └─Conv2d: 3-7                       [1, 192, 28, 28]          73,920
│    └─Sequential: 2-4                        [1, 192, 28, 28]          --
│    │    └─CNBlock: 3-8                      [1, 192, 28, 28]          306,048
│    │    └─CNBlock: 3-9                      [1, 192, 28, 28]          306,048
│    │    └─CNBlock: 3-10                     [1, 192, 28, 28]          306,048
│    └─Sequential: 2-5                        [1, 384, 14, 14]          --
│    │    └─LayerNorm2d: 3-11                 [1, 192, 28, 28]          384
│    │    └─Conv2d: 3-12                      [1, 384, 14, 14]          295,296
│    └─Sequential: 2-6                        [1, 384, 14, 14]          --
│    │    └─CNBlock: 3-13                     [1, 384, 14, 14]          1,201,920
│    │    └─CNBlock: 3-14                     [1, 384, 14, 14]          1,201,920
│    │    └─CNBlock: 3-15                     [1, 384, 14, 14]          1,201,920
│    │    └─CNBlock: 3-16                     [1, 384, 14, 14]          1,201,920
│    │    └─CNBlock: 3-17                     [1, 384, 14, 14]          1,201,920
│    │    └─CNBlock: 3-18                     [1, 384, 14, 14]          1,201,920
│    │    └─CNBlock: 3-19                     [1, 384, 14, 14]          1,201,920
│    │    └─CNBlock: 3-20                     [1, 384, 14, 14]          1,201,920
│    │    └─CNBlock: 3-21                     [1, 384, 14, 14]          1,201,920
│    └─Sequential: 2-7                        [1, 768, 7, 7]            --
│    │    └─LayerNorm2d: 3-22                 [1, 384, 14, 14]          768
│    │    └─Conv2d: 3-23                      [1, 768, 7, 7]            1,180,416
│    └─Sequential: 2-8                        [1, 768, 7, 7]            --
│    │    └─CNBlock: 3-24                     [1, 768, 7, 7]            4,763,136
│    │    └─CNBlock: 3-25                     [1, 768, 7, 7]            4,763,136
│    │    └─CNBlock: 3-26                     [1, 768, 7, 7]            4,763,136
├─AdaptiveAvgPool2d: 1-2                      [1, 768, 1, 1]            --
├─Sequential: 1-3                             [1, 17]                   --
│    └─LayerNorm2d: 2-9                       [1, 768, 1, 1]            1,536
│    └─Flatten: 2-10                          [1, 768]                  --
│    └─Sequential: 2-11                       [1, 17]                   --
│    │    └─Dropout: 3-27                     [1, 768]                  --
│    │    └─Linear: 3-28                      [1, 17]                   13,073
===============================================================================================
Total params: 27,833,201
Trainable params: 27,833,201
Non-trainable params: 0
Total mult-adds (Units.MEGABYTES): 321.62
===============================================================================================
Input size (MB): 0.60
Forward/backward pass size (MB): 131.27
Params size (MB): 111.31
Estimated Total Size (MB): 243.18
===============================================================================================
```
</details>

#### Detailed Classification Report (17 Classes)
```text
                                                                                        precision    recall  f1-score   support

  Glioma (Astrocitoma, Ganglioglioma, Glioblastoma, Oligodendroglioma, Ependimoma) T1       1.00      0.93      0.97        46
Glioma (Astrocitoma, Ganglioglioma, Glioblastoma, Oligodendroglioma, Ependimoma) T1C+       0.98      1.00      0.99        52
  Glioma (Astrocitoma, Ganglioglioma, Glioblastoma, Oligodendroglioma, Ependimoma) T2       0.89      0.97      0.93        34
                        Meningioma (Low Grade, Atypical, Anaplastic, Transitional) T1       0.97      1.00      0.99        35
                      Meningioma (Low Grade, Atypical, Anaplastic, Transitional) T1C+       0.98      1.00      0.99        62
                        Meningioma (Low Grade, Atypical, Anaplastic, Transitional) T2       0.94      0.97      0.96        33
                                                                             NORMAL T1       1.00      1.00      1.00        27
                                                                             NORMAL T2       0.97      1.00      0.98        29
                        Neurocitoma (Central - Intraventricular, Extraventricular) T1       1.00      1.00      1.00        17
                      Neurocitoma (Central - Intraventricular, Extraventricular) T1C+       1.00      1.00      1.00        26
                        Neurocitoma (Central - Intraventricular, Extraventricular) T2       1.00      0.82      0.90        11
        Other Types of Injuries (Abscesses, Cysts, Miscellaneous Encephalopathies) T1       1.00      1.00      1.00        15
      Other Types of Injuries (Abscesses, Cysts, Miscellaneous Encephalopathies) T1C+       1.00      1.00      1.00         5
        Other Types of Injuries (Abscesses, Cysts, Miscellaneous Encephalopathies) T2       1.00      1.00      1.00         5
                                    Schwannoma (Acoustic, Vestibular - Trigeminal) T1       1.00      1.00      1.00        16
                                  Schwannoma (Acoustic, Vestibular - Trigeminal) T1C+       1.00      1.00      1.00        19
                                    Schwannoma (Acoustic, Vestibular - Trigeminal) T2       1.00      0.77      0.87        13

                                                                             accuracy                           0.98       445
                                                                            macro avg       0.98      0.97      0.97       445
                                                                         weighted avg       0.98      0.98      0.98       445
```

#### Dataset Link (17-Class)
[Kaggle: Brain Tumor MRI Images (17 Classes)](https://www.kaggle.com/datasets/fernando2rad/brain-tumor-mri-images-17-classes)

</details>

<br/>

<details>
<summary>📑 View Technical Documentation: EfficientNetV2 (44-Class Model)</summary>

<br/>

#### Architecture Overview
The model follows a deep transfer learning approach with a custom classification head. It takes a `224x224x3` MRI input, passes it through the EfficientNetV2-S feature extractor, and terminates in a series of dense layers with batch normalization and dropout.

<p align="center">
  <img src="docs/training/model_architecture.png" width="450" alt="Model Architecture" />
</p>

#### Performance Metrics & Technical Evaluation
The model was rigorously evaluated across 44 distinct classes using a test set of 1,232 images. The high scores across all metrics demonstrate the model's reliability for clinical screening support.

---

#### Performance Metrics
- **Overall Accuracy: 97.0%**
- **Validation**: 96.69% average accuracy achieved via 5-fold cross-validation.

| Metric | Score | Description |
| :--- | :--- | :--- |
| **Accuracy** | **96.69%** | Overall correctness across all 44 tumor categories. |
| **Precision** | **98.0%** | Reliability of positive predictions (minimizing False Positives). |
| **Recall** | **97.0%** | Sensitivity to tumor detection (minimizing False Negatives). |
| **F1-Score** | **97.0%** | Harmonic mean of Precision and Recall. |

<p align="center">
  <img src="docs/training/kfold_results.png" width="55%" />
  <img src="docs/training/confusion_matrix.png" width="40%" />
</p>

#### Detailed Classification Report (44 Classes)
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

#### Dataset Link (44-Class)
[Kaggle: Brain Tumor MRI Images (44 Classes)](https://www.kaggle.com/datasets/fernando2rad/brain-tumor-mri-images-44c)

</details>

<br/>

### 📚 Medical Intelligence Database
- **Searchable Encyclopedia**: A dual-tab encyclopedia detailing both the 44-class (BTIS) specific pathologies and the 17-class (ConVext) broad diagnostic groups (including Gliomas, Meningiomas, Neurocytomas, Schwannomas, and other injuries).
- **Reference Library**: Extensive reference MRI images integrated to help users compare and learn about different tumor pathologies across both classification schemas.

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
