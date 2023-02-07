from ctypes import *
from numpy import *
from os import listdir
import numpy as np
import pandas as pd
import csv

file_name = "spy.csv"
df = pd.read_csv(file_name)
arr = df['days'].to_numpy()
last = arr[-1]
df['date']='day'
#df['MA']=df['SPY'].rolling(window=5).mean()
#print(list(df.columns))
xf = df.rolling(window=50).mean()
xf['date']='SMA50'
xf['days'] = pd.Series(arr)

af = df.rolling(window=200).mean()
af['date']='SMA200'
af['days'] = pd.Series(arr)
rf = pd.concat([df,xf,af],ignore_index=True, sort=False)
ma_spy = "new_spy.csv"
rf.to_csv(ma_spy,encoding='utf-8',index=False)

r_day = rf.loc[(rf['date'] == 'day') & (rf['days'] == last)]
r_50 = rf.loc[(rf['date'] == 'SMA50') & (rf['days'] == last)]
r_200 = rf.loc[(rf['date'] == 'SMA200') & (rf['days'] == last)]
xf = pd.concat([r_day,r_50,r_200],ignore_index=True, sort=False)
tf = xf.set_index('date').transpose()
tf['SM52']=(tf['SMA50']-tf['SMA200'])/tf['SMA50']*100
tf['SMd2']=(tf['day']-tf['SMA200'])/tf['day']*100
tf['SMd5']=(tf['day']-tf['SMA50'])/tf['day']*100
print(tf)
