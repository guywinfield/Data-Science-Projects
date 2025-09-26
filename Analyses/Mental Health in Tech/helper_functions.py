import pandas as pd
import numpy as np

from typing import Sequence

def df_col_minmax_grouped(df: pd.DataFrame, group_col: str, col: str, out_col: str | None=None) -> pd.DataFrame:
    out_col = out_col or f"{col}_scaled"
    df = df.copy()
    g = df.groupby(group_col)[col]
    min_g = g.transform('min')
    max_g = g.transform('max')
    denom = (max_g - min_g)
    # avoid divide-by-zero for constant groups
    df[out_col] = np.where(denom.eq(0), 0.0, (df[col] - min_g) / denom)
    return df


def df_col_pct_grouped(
    df: pd.DataFrame,
    group_col: str | list[str],
    col: str,
    out_col: str | None = None,
    decimals: int = 2,
) -> pd.DataFrame:
    """
    % of group SUM for `col`, computed within each group.
    Safely coerces `col` to numeric (non-numeric -> NaN).
    """
    out_col = out_col or f"{col}_pct"

    df = df.groupby([group_col, col]).agg(count=(col, "size")).reset_index()

    group_cols = [group_col] if isinstance(group_col, str) else list(group_col)

    # Coerce to numeric so '10', '1,000', '3.5' become numbers; bad values -> NaN
    s_num = pd.to_numeric(
        df["count"].astype(str).str.replace(",", "", regex=False),
        errors="coerce",
    )
    df["_num"] = s_num

    gsum = df.groupby(group_cols)["_num"].transform("sum")

    pct = np.where(
        gsum.eq(0) | gsum.isna(),
        np.nan,
        (df["_num"] / gsum) * 100,
    )

    df[out_col] = np.round(pct, decimals)

    return df.drop(columns=["_num"])