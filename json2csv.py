from numpy import *
import os
import numpy as np
import pandas as pd
import operator
import csv
import json
import subprocess
import sys
import re
from datetime import datetime
date_format = "%Y-%m-%d"

f = open('xdb_temp.json')
jdata = json.load(f)

sym = 'SPY'
df = pd.DataFrame(jdata[sym])
df.columns =['date',sym]

symbole = ['XLE','XLF','XLV','XLK','XLU','XLI','XLY','XLB','XLP','AAPL','MSFT','GOOGL','AMZN','TSLA']

for sym in symbole:
    xf = pd.DataFrame(jdata[sym])
    xf.columns =['date',sym]
    xf_p = xf[sym]
    df=pd.concat([df,xf_p],axis=1)

fst = df.loc[df.index[0],'date']
df['org'] = fst
print(df)
df['diff'] = pd.to_datetime(df['date'])-pd.to_datetime(df['org'])
print(df)
df['days']=(df['diff']).dt.total_seconds()/86400

df = df.drop(['org','diff'],axis=1)
print(df)
df.to_csv('spy.csv',encoding='utf-8',index=False)
exit()
