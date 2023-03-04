# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 0:37
# @Author  : Kenny Zhou
# @FileName: stock_df_base.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com

"""Base class for stock data frame."""

import pandas as pd

def check_stock_df(df: pd.DataFrame) -> bool:
    """Check if the data frame is a stock data frame."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    cols = ["date", "tic","open", "close", "high", "low", "volume","day"]

    for col in cols:
        if col not in df.columns:
            raise ValueError(f"df must contain {col} column")

    return True