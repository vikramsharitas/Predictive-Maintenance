import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Import Data
df = pd.read_csv('telemetry.csv', parse_dates=['datetime'], index_col='datetime')
fdf = pd.read_csv('failures.csv', parse_dates=['datetime'], index_col='datetime')
edf = pd.read_csv('errors.csv', parse_dates=['datetime'], index_col='datetime')

# Multiplicative Decomposition
result_volt = seasonal_decompose(df['volt'], model='multiplicative', extrapolate_trend='freq')
result_rot = seasonal_decompose(df['rotate'], model='multiplicative', extrapolate_trend='freq')
result_pre = seasonal_decompose(df['pressure'], model='multiplicative', extrapolate_trend='freq')
result_vib = seasonal_decompose(df['vibration'], model='multiplicative', extrapolate_trend='freq')

# Additive Decomposition
# result_add = seasonal_decompose(df['rotate'], model='additive', extrapolate_trend='freq')

# Plot
plt.rcParams.update({'figure.figsize': (30, 5)})
result_volt.trend.plot()
plt.figure()
result_rot.trend.plot()
plt.figure()
result_pre.trend.plot()
plt.figure()
result_vib.trend.plot()
"""fd_ex = fdf[fdf['failure'] == 'comp2'].copy()
ed_ex = edf.copy()
for px in fd_ex.index:
    plt.plot([px] * 2, [350, 500], color='tab:orange')
    print([px] * 2)
for cx in ed_ex.index:
    plt.plot([cx] * 2, [350, 500], color='tab:red')
    print([cx] * 2)"""
# result_add.plot().suptitle('Additive Decompose', fontsize=22)

plt.show()
