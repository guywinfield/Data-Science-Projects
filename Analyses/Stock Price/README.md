# 📈 Stock Market Analysis: US Big Five Tech Companies

### Analysis and predictive modeling of the "Big Five" tech stocks.

---

## 🎯 Goal & Scope

The purpose of this analysis is to explore the historical stock market data for the Big Five US technology companies—**Apple (AAPL), Microsoft (MSFT), Amazon (AMZN), Google (GOOGL), and Meta (META)**. By examining price movements, trading volume, and volatility, this study aims to understand market behavior and evaluate the effectiveness of various machine learning models for financial forecasting.

---

## 🧠 Key Insights

* **Monday Biais**: Looking at historical trading days there is a higher likelihood for better returns on a Monday whereas Fridays have the worst returns. This was proven to be statistically significant with a 0.05 alpha.
* **Apple has deep liquidity**: Throughout the period Apple traded on average 2.5x more shares (219M) than the next largest being Amazon (81M)  

### 📊 Modeling Approaches
The project implements a multi-faceted approach to stock prediction:
* **Time Series Forecasting**: Predicting future price points based on historical trends.
* **Survival Analysis**: Identifying the time to event of price volatility.
* **Ranking Approaches**: Identifying which stocks are likely to outperform others in a given period.


---

## 💻 Installation & Usage

### 1. Requirements
Ensure you have the following libraries installed:

```bash
pip install pandas numpy matplotlib seaborn yfinance duckdb lightgbm xgboost scikit-learn lifelines statsmodels