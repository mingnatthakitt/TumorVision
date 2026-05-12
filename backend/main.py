"""TumorVision FastAPI Backend — serves ML predictions for brain tumor classification."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import os
import io
from model_utils import predict_tumor, load_tumor_models


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load the ML model on startup."""
    load_tumor_models()
    yield


app = FastAPI(title="TumorVision API", lifespan=lifespan)

# CORS — allow frontend dev server and production origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Vite dev server
        "http://localhost:4173",   # Vite preview
        "http://localhost:3000",   # Fallback
        "https://*.hf.space",      # Hugging Face Spaces
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health check endpoint for frontend connectivity and Render.com."""
    from model_utils import model_44, model_17
    return {
        "status": "healthy",
        "models": {
            "44BTIS": model_44 is not None,
            "17ConVext": model_17 is not None
        }
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...), model_type: str = Form("44BTIS"), verify: bool = Form(False)):
    """
    Prediction endpoint that accepts an image and returns tumor classification.
    Optionally triggers MedGemma verification.
    """
    try:
        contents = await file.read()
        image_bytes = io.BytesIO(contents)
        
        # Call the prediction pipeline
        results = predict_tumor(image_bytes, model_type, run_verification=verify)
        return JSONResponse(content=results)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


# Serve static files from the frontend build directory
# Works for both local dev (backend/../frontend/dist) and Docker (/home/user/app/frontend/dist)
frontend_dist = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "dist"))

if os.path.exists(frontend_dist):
    # Serve all files in dist/ at the root path, except we'll handle the fallback manually
    app.mount("/static", StaticFiles(directory=frontend_dist), name="static")

    # Serve the main index.html for all other routes to support React Router
    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        # Prevent API routes from being intercepted
        if full_path.startswith("api/") or full_path in ["health", "predict"]:
            raise HTTPException(status_code=404)
        
        # Check if the requested file exists in dist (e.g., /TumorVision.png)
        file_path = os.path.join(frontend_dist, full_path)
        if os.path.isfile(file_path):
            return FileResponse(file_path)
            
        # Fallback to index.html for React Router
        return FileResponse(os.path.join(frontend_dist, "index.html"))


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
