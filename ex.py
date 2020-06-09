import pandas as pd
from dateutil.parser import parse
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import csv

pdf = pd.read_csv('telemetry.csv', parse_dates=['datetime'], index_col='datetime')
fdf = pd.read_csv('failures.csv', parse_dates=['datetime'], index_col='datetime')
edf = pd.read_csv('errors.csv', parse_dates=['datetime'], index_col='datetime')

plt.plot(pdf.index, pdf['pressure'], color='tab:blue')
plt.plot(pdf.index, pdf['volt'], color='tab:green')
plt.plot(pdf.index, pdf['vibration'], color='tab:cyan')
plt.plot(pdf.index, pdf['rotate'], color='tab:gray')
fd_ex = fdf[fdf['failure'] == 'comp2'].copy()
ed_ex = edf.copy()
for px in fd_ex.index:
    plt.plot([px] * 2, [0, 600], color='tab:orange')
for cx in ed_ex.index:
    plt.plot([cx] * 2, [600, -150], color='tab:red')
plt.show()
