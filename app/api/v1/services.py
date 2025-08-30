import pandas as pd
import joblib
import json
import random

from .schemas import PredictionRequest

class ModelService:

    def __init__(self, model_path: str, meta_path: str = None):
        self.model = joblib.load(model_path)
        
        if meta_path:
            with open(meta_path, 'r') as f:
                self.threshold = json.load(f).get("threshold")

    def predict(self, data: list[PredictionRequest]) -> dict:
        """Make a prediction using the loaded model."""

        X_new = pd.DataFrame([item.model_dump() for item in data])

        probability = self.model.predict_proba(X_new)[:, 1]
        prediction = self.model.predict(X_new)

        results = [
            {"probability": float(prob), "prediction": int(pred)} for prob, pred in zip(probability, prediction)
        ]

        return results

    def predict_with_threshold(self, data: list[PredictionRequest], threshold: float = None) -> dict:
        """Make a prediction using the loaded model with a threshold."""

        X_new = pd.DataFrame([item.model_dump() for item in data])

        probability = self.model.predict_proba(X_new)[:, 1]
        prediction = (probability >= (threshold if threshold is not None else self.threshold)).astype(int)

        results = [
            {"probability": float(prob), "prediction": int(pred)} for prob, pred in zip(probability, prediction)
        ]

        return results
    
    def generate_random(self, n: int) -> list[dict]:
        """Generate n random customer data samples."""

        genders = ["Male", "Female"]
        yesno = ["Yes", "No"]
        phone_service = ["Yes", "No"]
        multiple_lines = ["No phone service", "No", "Yes"]
        internet_service = ["DSL", "Fiber optic", "No"]
        online_security = ["Yes", "No", "No internet service"]
        online_backup = ["Yes", "No", "No internet service"]
        device_protection = ["Yes", "No", "No internet service"]
        tech_support = ["Yes", "No", "No internet service"]
        streaming_tv = ["Yes", "No", "No internet service"]
        streaming_movies = ["Yes", "No", "No internet service"]
        contract = ["Month-to-month", "One year", "Two year"]
        paperless_billing = ["Yes", "No"]
        payment_method = [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]

        samples = []
        for _ in range(n):
            tenure = random.randint(1, 72)
            monthly = round(random.uniform(18.25, 118.75), 2)
            total = round(monthly * tenure + random.uniform(-10, 10), 2)
            sample = {
                "gender": random.choice(genders),
                "SeniorCitizen": random.choice([0, 1]),
                "Partner": random.choice(yesno),
                "Dependents": random.choice(yesno),
                "tenure": tenure,
                "PhoneService": random.choice(phone_service),
                "MultipleLines": random.choice(multiple_lines),
                "InternetService": random.choice(internet_service),
                "OnlineSecurity": random.choice(online_security),
                "OnlineBackup": random.choice(online_backup),
                "DeviceProtection": random.choice(device_protection),
                "TechSupport": random.choice(tech_support),
                "StreamingTV": random.choice(streaming_tv),
                "StreamingMovies": random.choice(streaming_movies),
                "Contract": random.choice(contract),
                "PaperlessBilling": random.choice(paperless_billing),
                "PaymentMethod": random.choice(payment_method),
                "MonthlyCharges": monthly,
                "TotalCharges": total
            }
            samples.append(sample)
        return samples