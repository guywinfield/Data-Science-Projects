import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from rich.jupyter import display
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import shap

def find_outliers_sigmoid(data_series, z_threshold=2.5):
    """
    Identifies outliers based on the Z-score method.
    The Sigmoid rule is often implemented using a Z-score threshold.
    """
    mean = data_series.mean()
    std_dev = data_series.std()

    # Calculate Z-scores
    z_scores = (data_series - mean) / std_dev

    # Identify outliers using the threshold
    outlier_series = data_series[np.abs(z_scores) > z_threshold]

    # Note: Returns indices, values, and all Z-scores
    return outlier_series.index.tolist(), outlier_series.tolist(), z_scores

def summarise_model(y_test, y_pred):
    mae  = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2   = r2_score(y_test, y_pred)

    df = pd.DataFrame({
        "Metric": ["MAE", "RMSE", "R²"],
        "Value": [mae, rmse, r2]
    })

    return df


def ensure_all_features(X_input, feature_order):
    # Add missing columns
    for col in feature_order:
        if col not in X_input.columns:
            X_input[col] = 0

    # Ensure correct column order
    return X_input[feature_order]


def predict_with_explanation(input_dict, model, explainer, feature_order):

    X_input = pd.DataFrame([input_dict])
    X_input = ensure_all_features(X_input, feature_order)


    pred = model.predict(X_input)[0]
    pred_price = np.expm1(pred)

    shap_values = explainer.shap_values(X_input)

    # Force matplotlib backend
    shap.initjs()

    fig = shap.force_plot(
        explainer.expected_value,
        shap_values,
        X_input,
        matplotlib=True
    )

    plt.show()  # This renders the figure in PyCharm

    return pred_price


