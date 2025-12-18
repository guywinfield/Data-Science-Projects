import yfinance as yf
import pandas as pd
import numpy as np

def create_ticker_df(ticker, start_date, end_date):
    df = pd.DataFrame(
        yf.download(
            ticker,
            start=start_date,
            end=end_date,
            group_by="ticker",
            auto_adjust=True
        )
    ).droplevel(0, axis=1).reset_index()[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

    df['Ticker'] = ticker
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Volume'] = df['Volume'].astype(int) / 1000000



    df.columns = df.columns.str.lower()

    return df


def time_series_model_score(y_true, y_pred):
    mae = np.mean(np.abs(y_true - y_pred))
    mse = np.mean((y_true - y_pred) ** 2)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    bias_pct = np.mean(y_pred - y_true) / np.mean(y_true) * 100

    print(
        f"Mean Absolute Error: {mae} \n"
        f"Mean Squared Error: {mse} \n"
        f"Mean Absolute Percentage Error: {mape} \n"
        f"Forecast Bias (+ Overpredict - Underpredit): {bias_pct} \n"
    )

