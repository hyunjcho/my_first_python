import re
import json
import datetime
from datetime import date
import calendar
import ast
import numpy
import csv
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from numpy import arange

symbole = ['ZEN','CTXS','PZN','NUAN','TWTR']

# python remove.py
# copy.bat


f = open('xdb_main.json')
data = json.load(f)
#print(type(data))
print(data.keys())

for sym in symbole:
    data.pop(sym,None)
#list(map(data.__delitem__, filter(data.__contains__,symbole)))


#del data['AAPL']
print(data.keys())

fx = open('xdb_temp.json','w')
fx.write(json.dumps(data))
