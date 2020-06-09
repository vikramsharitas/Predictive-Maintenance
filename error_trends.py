import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
import csv

# Import Data
df = pd.read_csv('telemetry.csv', parse_dates=['datetime'], index_col='datetime')
fdf = pd.read_csv('failures.csv', parse_dates=['datetime'], index_col='datetime')
edf = pd.read_csv('errors.csv', parse_dates=['datetime'], index_col='datetime')

result_mul = seasonal_decompose(df['vibration'], model='multiplicative', extrapolate_trend='freq')
plt.rcParams.update({'figure.figsize': (30, 5)})
result_mul.trend.plot()
mean=result_mul.trend.mean()
plt.plot([min(df.index),max(df.index)],[mean]*2,color='tab:purple')
fd_ex = fdf[fdf['failure']=='comp4'].copy()
ed_ex = edf[edf['errorID']=='error5'].copy()
viblist=[]
for px in fd_ex.index:
    plt.plot([px] * 2, [20, 70], color='tab:orange')
    viblist.append(max(result_mul.trend.loc[px-timedelta(days=3):px-timedelta(days=1)]))
print(viblist)
for cx in ed_ex.index:
    plt.plot([cx] * 2, [20, 70], color='tab:red')
    #print([cx] * 2)
plt.show()

result_mul = seasonal_decompose(df['rotate'], model='multiplicative', extrapolate_trend='freq')
plt.rcParams.update({'figure.figsize': (30, 5)})
result_mul.trend.plot()
mean=result_mul.trend.mean()
plt.plot([min(df.index),max(df.index)],[mean]*2,color='tab:purple')
fd_ex = fdf[fdf['failure']=='comp2'].copy()
ed2_ex = edf[edf['errorID']=='error2'].copy()
ed3_ex = edf[edf['errorID']=='error3'].copy()
rotlist=[]
for px in fd_ex.index:
    plt.plot([px] * 2, [350, 500], color='tab:orange')
    rotlist.append(min(result_mul.trend.loc[px-timedelta(days=3):px-timedelta(days=1)]))
print(rotlist)
for cx2 in ed2_ex.index:
    plt.plot([cx2] * 2, [350, 500], color='tab:red')
   # print([cx2] * 2)
for cx3 in ed3_ex.index:
    plt.plot([cx3] * 2, [300, 550], color='tab:olive')
    #print([cx3] * 2)
plt.show()

result_mul = seasonal_decompose(df['volt'], model='multiplicative', extrapolate_trend='freq')
plt.rcParams.update({'figure.figsize': (30, 5)})
result_mul.trend.plot()
mean=result_mul.trend.mean()
plt.plot([min(df.index),max(df.index)],[mean]*2,color='tab:purple')
fd_ex = fdf[fdf['failure']=='comp1'].copy()
ed_ex = edf[edf['errorID']=='error1'].copy()
vollist=[]
for px in fd_ex.index:
    plt.plot([px] * 2, [150, 200], color='tab:orange')
    vollist.append(max(result_mul.trend.loc[px-timedelta(days=3):px-timedelta(days=1)]))
print(vollist)
for cx in ed_ex.index:
    plt.plot([cx] * 2, [150, 200], color='tab:red')
   # print([cx] * 2)
plt.show()

result_mul = seasonal_decompose(df['pressure'], model='multiplicative', extrapolate_trend='freq')
plt.rcParams.update({'figure.figsize': (30, 5)})
result_mul.trend.plot()
mean=result_mul.trend.mean()
plt.plot([min(df.index),max(df.index)],[mean]*2,color='tab:purple')
fd_ex = fdf[fdf['failure']=='comp3'].copy()
ed_ex = edf[edf['errorID']=='error4'].copy()
prelist=[]
for px in fd_ex.index:
    plt.plot([px] * 2, [80, 140], color='tab:orange')
    prelist.append(max(result_mul.trend.loc[px-timedelta(days=3):px-timedelta(days=1)]))
print(prelist)
for cx in ed_ex.index:
    plt.plot([cx] * 2, [80, 140], color='tab:red')
    #print([cx] * 2)
plt.show()