from fastapi import APIRouter, Query
from .services import ModelService
from .schemas import PredictionRequest
import os


api_v1_router = APIRouter(prefix="/api/v1")

project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../"))
model_path = os.path.join(project_root, "models", "logreg_pipeline.joblib")
meta_path = os.path.join(project_root, "models", "decision_threshold.json")

model_service = ModelService(model_path, meta_path)

@api_v1_router.get("/status")
def get_status():
    return {"status": "ok"}

@api_v1_router.get("/threshold")
def get_threshold():
    return {"threshold": model_service.threshold}

@api_v1_router.post(
    "/predict",
    summary="Predict customer churn",
    response_description="Predicted churn for each customer"
)
def predict(data: list[PredictionRequest]):
    prediction = model_service.predict_with_threshold(data)
    return prediction

@api_v1_router.get(
    "/random",
    summary="Generate random customer data",
    response_description="Randomly generated customer data for testing"
)
def random_customers(
    n: int = Query(1, ge=1, le=10, description="Number of random samples to generate (1-10)")
):
    """
    Generate a random list of customer data samples for testing the /predict endpoint.
    """
    samples = model_service.generate_random(n)
    return samples