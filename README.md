# Customer Churn Predictor API

*A complete end-to-end machine learning project using the Telco Customer Churn dataset, featuring model training, evaluation, and deployment as a production-ready API.*

---

## 🚀 Introduction

Welcome! This project is part of my AI/ML learning journey. I’ve always been fascinated by how data can predict customer behavior, and churn prediction is a classic, high-impact use case. Customer churn is costly—predicting who will leave enables proactive retention strategies.

This repository demonstrates a full-stack ML workflow: from data exploration and preprocessing in Jupyter, through model training and evaluation with scikit-learn, to serving predictions via a FastAPI microservice, all containerized with Docker for easy deployment.

---

## 📊 Dataset

- **Source:** [Kaggle Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Shape:** 7,043 customers × 21 features
- **Target:** `Churn` (Yes/No)
- **Features:** Demographics, services (DSL/Fiber optic, streaming), billing, tenure, and more
- **Preprocessing:**
  - Handled missing values
  - Scaled numeric features (`StandardScaler`)
  - Encoded categorical features (`OneHotEncoder`)
  - See [notebooks/exploratory.ipynb](notebooks/exploratory.ipynb) for full EDA and pipeline

---

## 🛠️ Approach

- **Model:** Logistic Regression (chosen for interpretability and as a strong baseline)
- **Pipeline:** `ColumnTransformer` for scaling and one-hot encoding
- **Class Imbalance:** Addressed with `class_weight="balanced"`
- **Evaluation:** ROC/AUC, Precision-Recall curve, confusion matrix
- **Threshold Tuning:** Custom threshold selection to balance recall and precision for business needs
- **Deployment:** Model and threshold saved with `joblib` and JSON, loaded by the FastAPI app

---

## 📈 Results

- **AUC:** 0.84 (strong discriminative ability)
- **Recall:** 78% (model catches most churners)
- **Precision:** 51% (about half of predicted churns are false positives—acceptable for retention-focused strategies)
- **Key Insights:**
  - Fiber optic customers churn more than DSL
  - Longer tenure reduces churn risk
  - Contract type is a key driver (month-to-month customers churn more)
- *The model isn’t perfect, but it’s a solid first step in showing how AI can highlight customer risk and guide retention strategies.*

---

## 🖥️ API Usage

### 🌐 Live Demo

The API is deployed and accessible here:  
👉 [Customer Churn Predictor API (GCP Deployment)](https://churn.solvin.co/docs)

### Run Locally

```bash
uvicorn app.main:app --reload --reload-dir app
```

### Docker

```bash
docker build -f docker/Dockerfile -t customer-churn-api .
docker run --env-file .env -p 8000:80 customer-churn-api
```

### Example Request

```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 5,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 89.10,
  "TotalCharges": 450.50
}
```

### Example Response

```json
[
  {
    "probability": 0.73,
    "prediction": 1
  }
]
```

- `probability`: Probability of churn (float)
- `prediction`: 1 = churn, 0 = no churn (using the tuned threshold)

---

## 📂 Project Structure

```
├── app/                # FastAPI app (API, services, schemas)
├── models/             # Saved pipeline (.joblib) and threshold (.json)
├── data/               # Dataset (CSV)
├── notebooks/          # Jupyter notebooks for EDA and training
├── tests/              # Pytest configuration and fixtures
├── docker/             # Dockerfile and compose
├── requirements.txt    # Python dependencies
├── README.md
```

---

## ☁️ Deployment

- Dockerized for portability and reproducibility
- Designed for deployment on cloud platforms (e.g., GCP)
- Future: Add a simple Flask web UI for non-technical users to test predictions

---

## 🔭 Future Work

- Feature engineering (interaction terms, derived features)
- Try tree-based models (Random Forest, XGBoost)
- Hyperparameter tuning
- CI/CD pipeline with GitHub Actions

---

## 📄 License

MIT License (open-source, permissive)

---

## 🙏 Acknowledgments

- Dataset: Kaggle Telco Customer Churn
- Libraries: scikit-learn, pandas, FastAPI, joblib, matplotlib, seaborn

---

### ✨ Recruiter-Friendly Closing Note

> This project represents my first end-to-end machine learning pipeline. It combines data preprocessing, model training, evaluation, and deployment into an API. More than just accuracy numbers, I wanted to learn how to make models usable in real business contexts. This repo is a snapshot of my learning journey and my excitement about applying AI to solve meaningful problems.