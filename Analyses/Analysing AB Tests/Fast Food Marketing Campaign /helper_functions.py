import pandas as pd
import numpy as np


def bootstrap_median(original_sample: pd.DataFrame, label: str, replications: int) -> np.ndarray:
    """Return an array of bootstrap medians for `label`."""
    medians = np.empty(replications)
    n = len(original_sample)
    for i in range(replications):
        resample = original_sample[label].sample(n, replace=True)
        medians[i] = resample.median()
    return medians