import yfinance as yf
import pandas as pd
import numpy as np


def safe_digitize(x, bins):
    return int(np.digitize(x, bins[1:-1], right=False))


def get_state(row, current_position, POSITION_TO_STATE):
    return (
        int(row["regime_id"]),
        int(row["trend_bucket"]),
        int(row["vol_bucket"]),
        int(row["mom_bucket"]),
        POSITION_TO_STATE[current_position]
    )


def train_q_learning(
    data,
    POSITION_TO_STATE,
    ACTION_TO_POSITION,
    n_episodes=200,
    alpha=0.1,
    gamma=0.95,
    epsilon=1.0,
    epsilon_decay=0.995,
    epsilon_min=0.05,
    transaction_cost=0.001,
):
    q_table = {}
    episode_rewards = []

    for episode in range(n_episodes):
        total_reward = 0.0
        current_position = 0

        for t in range(len(data) - 1):
            row = data.iloc[t]
            state = get_state(row, current_position, POSITION_TO_STATE)

            if state not in q_table:
                q_table[state] = np.zeros(3)

            if np.random.rand() < epsilon:
                action = np.random.choice([0, 1, 2])
            else:
                action = int(np.argmax(q_table[state]))

            new_position = ACTION_TO_POSITION[action]
            market_return = data.iloc[t + 1]["close_pct_daily_change"]
            reward = (
                new_position * market_return
                - transaction_cost * abs(new_position - current_position)
            )

            next_state = get_state(
                data.iloc[t + 1], new_position, POSITION_TO_STATE
            )

            if next_state not in q_table:
                q_table[next_state] = np.zeros(3)

            best_next_q = np.max(q_table[next_state])
            old_q = q_table[state][action]

            q_table[state][action] = old_q + alpha * (
                reward + gamma * best_next_q - old_q
            )

            current_position = new_position
            total_reward += reward

        epsilon = max(epsilon_min, epsilon * epsilon_decay)
        episode_rewards.append(total_reward)

    return q_table, episode_rewards


def run_policy(data, q_table, POSITION_TO_STATE, ACTION_TO_POSITION, transaction_cost=0.001):
    rows = []
    current_position = 0
    portfolio_value = 1.0

    for t in range(len(data) - 1):
        row = data.iloc[t]
        state = get_state(row, current_position, POSITION_TO_STATE)

        if state in q_table:
            action = int(np.argmax(q_table[state]))
        else:
            action = 1  # default to flat if unseen state

        new_position = ACTION_TO_POSITION[action]
        market_return = data.iloc[t + 1]["close_pct_daily_change"]
        strategy_return = (
            new_position * market_return
            - transaction_cost * abs(new_position - current_position)
        )

        portfolio_value *= (1 + strategy_return)

        rows.append({
            "date": data.iloc[t + 1]["date"],
            "action": action,
            "position": new_position,
            "market_return": market_return,
            "strategy_return": strategy_return,
            "portfolio_value": portfolio_value,
            "regime_name": data.iloc[t + 1]["regime_name"]
        })

        current_position = new_position

    return pd.DataFrame(rows)


def sharpe_ratio(returns, periods_per_year=252):
    returns = pd.Series(returns).dropna()
    if returns.std() == 0:
        return np.nan
    return np.sqrt(periods_per_year) * returns.mean() / returns.std()


def max_drawdown(portfolio_values):
    s = pd.Series(portfolio_values)
    rolling_max = s.cummax()
    dd = s / rolling_max - 1
    return dd.min()