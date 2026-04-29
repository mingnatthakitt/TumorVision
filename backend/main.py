"""TumorVision FastAPI Backend — serves ML predictions for brain tumor classification."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import io
from model_utils import predict_tumor, load_tumor_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load the ML model on startup."""
    load_tumor_model()
    yield


app = FastAPI(title="TumorVision API", lifespan=lifespan)

# CORS — allow frontend dev server and production origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Vite dev server
        "http://localhost:4173",   # Vite preview
        "http://localhost:3000",   # Fallback
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health check endpoint for frontend connectivity and Render.com."""
    from model_utils import model
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Accept an MRI image upload and return top-3 tumor type predictions.
    """
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Please upload a JPG or PNG image."
        )

    try:
        contents = await file.read()
        result = predict_tumor(io.BytesIO(contents))

        if "error" in result:
            raise HTTPException(status_code=503, detail=result["error"])

        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
