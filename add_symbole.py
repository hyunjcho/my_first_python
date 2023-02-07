import json
import csv
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='AS0C1JP1LQY65GBK')
f = open('xdb_main.json')
config = json.load(f)
print(config.keys())

# copy.bat
# python add_symbole.py
# python clean_up.py
# copy xdb_clean.json xdb_temp.json
# copy.bat

with open("symbole.txt", "r") as infile:
    data = [data.rstrip() for data in infile]

symbole = eval(data[0])

for sym in symbole:
    data, meta_data = ts.get_daily(sym,outputsize='full')
    keys = sorted(data.keys())
    dic = {}

    for item in keys:
        value = data[item]['4. close']
        dic[item] = value

    d = [{'date':key,'price':value} for key,value in dic.items()]
    config[sym]=d

print(config.keys())

fx = open('xdb_temp.json','w')
fx.write(json.dumps(config))

