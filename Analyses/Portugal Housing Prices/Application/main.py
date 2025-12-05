import json
import base64
import io
import numpy as np
import pandas as pd
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import matplotlib
matplotlib.use("Agg")   # 👈 THIS FIXES THE ERROR
import matplotlib.pyplot as plt

from pydantic import BaseModel
from catboost import CatBoostRegressor
import shap
import joblib

# ------------------------------
# Load model + metadata + SHAP
# ------------------------------
model = CatBoostRegressor()
model.load_model("model.cbm")

with open("metadata.json", "r") as f:
    metadata = json.load(f)

categorical_cols = metadata["categorical_cols"]
feature_order = metadata["feature_order"]

explainer = joblib.load("explainer.pkl")

app = FastAPI()

templates = Jinja2Templates(directory="templates")


# ------------------------------
# Utility functions
# ------------------------------
def preprocess_form_input(d):
    # Convert to dict (in case it's a Pydantic model)
    d = dict(d).copy()

    # ------------------------------------------------------
    # 1. Base categorical variables
    # ------------------------------------------------------
    cat_defaults = {
        "District": "Unknown",
        "Type": "Unknown",
        "EnergyCertificate": "Unknown",
        "ConservationStatus": "Unknown"
    }

    for col, default in cat_defaults.items():
        d[col] = str(d.get(col, default)).strip() or default

    # ------------------------------------------------------
    # 2. Base numeric variables
    # ------------------------------------------------------
    num_defaults = {
        "TotalArea": 0.0,
        "LivingArea": 0.0,
        "TotalRooms": 0.0,
        "NumberOfWashrooms": 0.0,
        "ConstructionYear": 0,
        "FloorNum": 0,
        "Parking": 0.0,
        "Elevator": 0.0,
        "Garage": 0.0,
        "ElectricCarsCharging": 0.0
    }

    for col, default in num_defaults.items():
        val = d.get(col, default)
        if val in ("", None):
            val = default
        d[col] = float(val) if isinstance(default, float) else int(val)

    # ------------------------------------------------------
    # 3. Engineered features
    # ------------------------------------------------------

    # (a) Lisbon / Porto flag
    d["IsLisbonOrPorto"] = 1 if d["District"] in ["Lisbon", "Porto"] else 0

    # (b) Age at sale (using 2025 as reference year)
    d["AgeAtSale"] = 2025 - d["ConstructionYear"] if d["ConstructionYear"] > 0 else 0

    # (c) Washroom ratio
    if d["TotalRooms"] > 0:
        d["WashroomRatio"] = d["NumberOfWashrooms"] / d["TotalRooms"]
    else:
        d["WashroomRatio"] = 0

    # ------------------------------------------------------
    # 4. Ensure all model-required columns exist
    # ------------------------------------------------------
    # Insert placeholder for any missing features with a default of 0
    for col in feature_order:
        if col not in d:
            d[col] = 0

    # ------------------------------------------------------
    # 5. Build dataframe in correct order
    # ------------------------------------------------------
    df = pd.DataFrame([[d[col] for col in feature_order]], columns=feature_order)

    # Ensure categorical cols are strings
    for col in categorical_cols:
        df[col] = df[col].astype(str)

    return df


def shap_plot_base64(shap_values):
    fig, ax = plt.subplots(figsize=(8, 4))
    shap.plots.bar(shap_values, max_display=10, show=False)

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)

    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode("utf-8")


# ------------------------------
# Browser UI — GET /
# ------------------------------
@app.get("/", response_class=HTMLResponse)
def form_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ------------------------------
# Browser POST — Predict + SHAP
# ------------------------------
@app.post("/predict_form", response_class=HTMLResponse)
def predict_form(
    request: Request,
    District: str = Form(...),
    Type: str = Form(...),
    EnergyCertificate: str = Form(None),
    TotalArea: float = Form(...),
    LivingArea: float = Form(None),
    TotalRooms: float = Form(...),
    NumberOfWashrooms: float = Form(...),
    ConstructionYear: int = Form(...),
    FloorNum: int = Form(...),
    Parking: int = Form(None),
    Elevator: int = Form(None),
    Garage: int = Form(None),
    ConservationStatus: str = Form(None),
    ElectricCarsCharging: int = Form(None)
):

    # Build input dict
    data = {
        "District": District,
        "Type": Type,
        "EnergyCertificate": EnergyCertificate,
        "TotalArea": TotalArea,
        "LivingArea": LivingArea,
        "TotalRooms": TotalRooms,
        "NumberOfWashrooms": NumberOfWashrooms,
        "ConstructionYear": ConstructionYear,
        "FloorNum": FloorNum,
        "Parking": Parking,
        "Elevator": Elevator,
        "Garage": Garage,
        "ConservationStatus": ConservationStatus,
        "ElectricCarsCharging": ElectricCarsCharging
    }

    df = preprocess_form_input(data)

    # Predict
    pred_log = model.predict(df)[0]
    prediction = float(np.expm1(pred_log))

    # SHAP explanation
    shap_values = explainer(df)
    shap_image = shap_plot_base64(shap_values[0])

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": f"€{prediction:,.0f}",
            "shap_image": shap_image
        }
    )