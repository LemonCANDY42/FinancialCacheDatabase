# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 0:04
# @Author  : Kenny Zhou
# @FileName: data_container.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com

"""Persist the cached data stream to the database.
"""

import os
from pathlib import Path

import pandas as pd
import sqlite3
from datetime import datetime

from database.stock_df_base import check_stock_df

from tqdm import tqdm

class DataContainer:
  """将pandas类的数据持久化为sqlite数据库
  """
  def __init__(self,path:str,database_name:str = "stocks.db"):
    path = Path(path)
    if path.is_dir() and not path.exists():
      path.mkdir(parents=True)
      path+=database_name
    elif path.is_dir() and path.exists():
      path+=database_name
    elif path.suffix == ".db" or path.suffix == ".sqlite" or path.suffix == ".sqlite3":
      pass
    else:
        raise TypeError("path must be a directory or file")

    self.path = path

    self._connect()
    self._cursor = self._conn.cursor()

  def _connect(self):
    """连接数据库"""
    try:
      self._conn = sqlite3.connect(self.path)
    except Exception as e:
      raise e
    else:
      print("数据库连接成功！")

  def _update_database(self):
    """更新数据库
    """
    pass

  def to_sql(self, df: pd.DataFrame, name="default",if_exists="fail"):
    """将数据写入数据库
        df: pandas.DataFrame
        name: 表名
        if_exists: fail,replace,append
    """

    try:
      df.to_sql(name, self._conn, if_exists=if_exists)
    except Exception as e:
      raise e
    else:
      print("写入数据库成功！")

  def read_sql(self, name="default"):
    """从数据库中读取数据
        name: 表名
    """
    try:
      df = pd.read_sql(f"SELECT * FROM '{name}'", self._conn)
    except Exception as e:
      raise e
    else:
      print("读取数据库成功！")
      return df


if __name__ == '__main__':
  path = r"D:\github\FinancialCacheDatabase\database\test.db"
  # df = pd.DataFrame({"a":[1,2,3],"b":[4,5,6]})
  df = pd.read_csv(r"E:\github\FinRL\data\DOW_30_TICKER_2005-01-01_2020-07-01.csv",index_col=[0])
  dc = DataContainer(path)
  dc.to_sql(df,if_exists="append")
  df = dc.read_sql()
  print(df)