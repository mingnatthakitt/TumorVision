# ── Stage 1: Build React Frontend ──
FROM node:20-slim AS frontend-builder

WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build


# ── Stage 2: Python Backend + Serve Frontend ──
FROM python:3.10-slim

# System deps for TensorFlow + HDF5
RUN apt-get update && apt-get install -y --no-install-recommends \
    libhdf5-dev \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user (required by Hugging Face Spaces)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR /home/user/app

# Install Python dependencies
COPY --chown=user backend/requirements.txt ./backend/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r backend/requirements.txt

# Copy backend source
COPY --chown=user backend/ ./backend/

# Copy built frontend from Stage 1
COPY --from=frontend-builder --chown=user /app/frontend/dist ./frontend/dist

# Expose HF Spaces port
EXPOSE 7860

# Start FastAPI — HF Spaces requires port 7860
WORKDIR /home/user/app/backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
