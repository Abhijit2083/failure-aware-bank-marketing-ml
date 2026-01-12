from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="Bank Marketing Prediction API")

# Load model
model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prob = model.predict_proba(df)[0][1]
    pred = int(prob >= 0.5)

    return {
        "subscription_probability": round(float(prob), 4),
        "prediction": "yes" if pred == 1 else "no"
    }
