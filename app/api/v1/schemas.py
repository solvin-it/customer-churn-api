from pydantic import BaseModel, Field
from typing import Optional

class PredictionRequest(BaseModel):
    """
    Request schema for customer churn prediction.
    Each field corresponds to a customer attribute required by the model.
    """
    gender: str = Field(..., description="Gender of the customer (Male/Female)")
    SeniorCitizen: int = Field(..., description="Whether the customer is a senior citizen (1, 0)")
    Partner: str = Field(..., description="Whether the customer has a partner (Yes/No)")
    Dependents: str = Field(..., description="Whether the customer has dependents (Yes/No)")
    tenure: int = Field(..., description="Number of months the customer has stayed")
    PhoneService: str = Field(..., description="Whether the customer has phone service (Yes/No)")
    MultipleLines: str = Field(..., description="Whether the customer has multiple lines")
    InternetService: str = Field(..., description="Type of internet service (DSL/Fiber optic/No)")
    OnlineSecurity: str = Field(..., description="Whether the customer has online security (Yes/No/No internet service)")
    OnlineBackup: str = Field(..., description="Whether the customer has online backup (Yes/No/No internet service)")
    DeviceProtection: str = Field(..., description="Whether the customer has device protection (Yes/No/No internet service)")
    TechSupport: str = Field(..., description="Whether the customer has tech support (Yes/No/No internet service)")
    StreamingTV: str = Field(..., description="Whether the customer has streaming TV (Yes/No/No internet service)")
    StreamingMovies: str = Field(..., description="Whether the customer has streaming movies (Yes/No/No internet service)")
    Contract: str = Field(..., description="Contract type (Month-to-month/One year/Two year)")
    PaperlessBilling: str = Field(..., description="Whether the customer has paperless billing (Yes/No)")
    PaymentMethod: str = Field(..., description="Payment method")
    MonthlyCharges: float = Field(..., description="The amount charged to the customer monthly")
    TotalCharges: float = Field(..., description="The total amount charged to the customer")

class PredictionResponse(BaseModel):
    pass