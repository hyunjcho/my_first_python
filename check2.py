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
from collections import defaultdict



def grep(l, s):
    return [i for i in l if s in i]

def date_open(d_ago,data_str):
    today = datetime.date.today()
    days_ago = d_ago
    i = 0
    while i<5:
        thirty_day = datetime.timedelta(days=days_ago)
        sd = today - thirty_day
        some_day = '{:%Y-%m-%d}'.format(sd)
        print('{0} days ago from today is {1} {2}'.format(days_ago,sd,calendar.day_name[sd.weekday()]))
        search_result = re.search(some_day,data_str)
        if search_result is not None:
            print('good')
            final_day = some_day
            break
        else:
            print('no good')
            days_ago = days_ago - 1
            final_day = some_day
        i= i + 1
    
    return final_day

name = ["C:\\Users\\jinc.SILVACOCORP.000\\OneDrive\\Script\\xdb_main.json","C:\\Users\\jinc.SILVACOCORP.000\\OneDrive\\Script\\xdb_temp.json"]
#print(name,type(name))

array=[]
new_dict = defaultdict(dict)

for nx in name:
    f = open(nx)
    data = json.load(f)
    symbole = list(data.keys())

    for sym in symbole:
        rickon=dict()
        result = dict()
        result = data[sym]
        dic = dict()
        for value_dict in result:
            dic[value_dict['date']]=float(value_dict['price'])


        latest_price= list(dic.values())[-1] 
        latest_date = list(dic.keys())[-1]
        two_date = list(dic.keys())[-2]
        new_dict[nx][sym]='{0} {1:5.2f} {2} {3}'.format(latest_date,latest_price,two_date,sym)

for sym in symbole:
    print('{0:50} {1}'.format(new_dict[name[0]][sym],new_dict[name[1]][sym]))

print('{0:50} {1}'.format(name[0],name[1]))
