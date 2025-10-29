import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def abline(ax , b, m, *args , ** kwargs):
    "Add a line with slope m and intercept b to ax"
    xlim = ax. get_xlim ()
    ylim = [m * xlim [0] + b, m * xlim [1] + b]
    ax.plot(xlim , ylim , *args , ** kwargs)


def plot_residuals_leverage(fitted_results):
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))

    # Chart 1 — Residuals vs Fitted
    sns.scatterplot(x=fitted_results.fittedvalues, y=fitted_results.resid, ax=ax[0])
    ax[0].axhline(y=0, linestyle='--', linewidth=1, color='k')
    ax[0].set_title("Residuals vs Fitted")
    ax[0].set_xlabel("Fitted values")
    ax[0].set_ylabel("Residuals")

    # Chart 2 — Leverage (hat values)
    infl = fitted_results.get_influence()
    hat = infl.hat_matrix_diag  # 1D array of length nobs
    sns.scatterplot(x=np.arange(int(fitted_results.nobs)), y=hat, ax=ax[1])
    ax[1].set_title("Leverage (Hat) Values")
    ax[1].set_xlabel("Observation index")
    ax[1].set_ylabel("Hat value")

    plt.tight_layout()
    plt.show()

