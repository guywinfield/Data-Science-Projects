from fastapi import FastAPI
from pydantic import BaseModel, conlist
import joblib
import numpy as np

app = FastAPI(title="Iris Classifier API")

# Load the saved model
model = joblib.load("model.pkl")

# Define expected input schema
class IrisFeatures(BaseModel):
    features: conlist(float, min_length=4, max_length=4)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: IrisFeatures):
    input_array = np.array(data.features).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    probabilities = model.predict_proba(input_array)[0].tolist()
    return {
        "prediction": int(prediction),
        "class_probabilities": probabilities
    }