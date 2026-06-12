from fastapi import FastAPI

from database import engine
from models import Base

from routers.patients import router as patient_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Health Prediction System",
    description="AI-powered healthcare prediction application",
    version="1.0.0"
)

app.include_router(patient_router)


@app.get("/")
def home():
    return {
        "message": "Health Prediction API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }