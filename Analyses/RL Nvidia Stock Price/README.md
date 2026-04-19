# 🤖 Reinforcement Learning Trading Agent: NVIDIA Stock

### Learning a trading strategy using Q-learning on NVIDIA (NVDA)

---

## 🎯 Goal & Scope

The purpose of this project is to build and evaluate a **Reinforcement Learning (RL) trading agent** that learns how to make buy, sell, and hold decisions based on historical stock data.

Rather than predicting prices directly, this notebook focuses on:
- Learning **optimal trading decisions**
- Maximising **cumulative profit over time**
- Understanding how market conditions influence trading behaviour

The model is trained and tested on historical NVIDIA stock data, using engineered features such as volatility, momentum, and trend signals.

---

## 🧠 Key Insights

- **Markets behave differently under different conditions**: High volatility periods (e.g. COVID crash) create very different trading environments compared to stable periods.
- **Feature engineering is critical**: Signals like momentum, volatility, and trend strength provide the foundation for decision-making.
- **RL focuses on actions, not predictions**: The agent learns *what to do*, not *what will happen*.
- **Ensemble agents improve stability**: Combining multiple trained agents reduces randomness and improves robustness.


---

## 📊 Modeling Approach

This project uses a **Reinforcement Learning framework** rather than traditional supervised learning:

- **Q-Learning (Tabular RL)**  
  Learns a mapping from states to optimal actions using reward signals.

- **Discretisation Strategy**  
  Converts continuous features into categorical states for tractability.

- **Ensemble Methods**  
  Combines multiple trained agents for more robust decision-making.

---

## 💻 Installation & Usage

### 1. Requirements

```bash
pip install pandas numpy matplotlib seaborn yfinance scikit-learn