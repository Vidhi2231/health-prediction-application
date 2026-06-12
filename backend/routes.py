from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {
        "message": "Health Prediction API Running"
    }

@router.get("/health")
def health():
    return {
        "status": "ok"
    }