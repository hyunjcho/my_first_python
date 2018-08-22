import json
import sys
import csv
from alpha_vantage.timeseries import TimeSeries

f = open('xdb3.json')
fx = open('xdb4.json','w')
#
#
#You can update anytime you want as long as xdb2.json is golden
#Remember you need to copy xdb3.json to xdb2.json after market close
#analysis program access xdb3.json
#
#

org = json.load(f)
symx = list(org.keys())
symbole = symx[99:]
print(symbole)

ts = TimeSeries(key='AS0C1JP1LQY65GBK')
data, meta_data = ts.get_batch_stock_quotes(symbole)

#print(data)
#print(type(data))

mydict = {}
for item in data:
    dsym=list(item.values())[0]
    dpri=list(item.values())[1]
    mydict[dsym] = dpri 

dd = list(item.values())[3]
latest_day = dd.split(" ")[0]


symb = list(mydict.keys())

for sym in symb:
    s = {'date': latest_day, 'price': mydict[sym]}
    org[sym].append(s)

fx.write(json.dumps(org))
