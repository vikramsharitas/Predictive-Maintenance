import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv("FutureTech.csv")
df_1 = df.loc[df['machineID']==1]

from statsmodels.tsa.seasonal import seasonal_decompose
df_1['datetime'] = pd.to_datetime(df_1['datetime'])
df_1.set_index('datetime',inplace=True)

y = df_1['Voltage'].resample('D').sum()

import statsmodels.api as sm
decomposition = sm.tsa.seasonal_decompose(y, model='multiplicative')
decomposition.seasonal.plot()