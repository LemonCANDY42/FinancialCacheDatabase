import yfinance as yf  
import matplotlib.pyplot as plt
import pandas as pd

START_TIME = '2017-01-01'
END_TIME = '2021-12-01'
#,'QQQ','SQQQ','TQQQ'
data = yf.download(['AMZN', 'AAPL', 'FB', 'WMT', 'TSM', 'TSLA', 'NVDA', 'BABA', 'NTES'],'2000-01-01','2022-12-01')
data = data.fillna(value=0)
data.to_csv('../Data/US.csv')
print(data)

# test=pd.read_csv('./datas/US.csv',header=[0,1], index_col=0)
# print(test)
# test["Adj Close"].plot()
# plt.show()