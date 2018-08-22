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
        #print('{0} days ago from today is {1} {2}'.format(days_ago,sd,calendar.day_name[sd.weekday()]))
        search_result = re.search(some_day,data_str)
        if search_result is not None:
            #print('good')
            final_day = some_day
            break
        else:
            #print('no good')
            days_ago = days_ago + 1
            final_day = some_day
        i= i + 1
    
    return final_day

fc = open('comment.csv')
reader = csv.reader(fc)
mydict = {}
for row in reader:
    mydict[row[0]] = row[1]

#print(mydict)

#
#
# read_json.py uses xdb3.json db
#
#
f = open('xdb4.json')
data = json.load(f)
#print(data.keys())
symbole = list(data.keys())
#print(symbole)

aa=data['AAPL']
data_str = json.dumps(aa) 
d_year = 364
year_day=date_open(d_year,data_str)

list_day = [1,5,30,60,90,120,364]
some_day = list()
i=0;
for baelish in list_day:
    arya_day=date_open(baelish,data_str)
    some_day.append(arya_day)
    print(some_day)


jorah = {}
for sym in symbole:
    rickon=dict()
    result = dict()
    #print(sym)
    result = data[sym]
    #dic is the new dictionary which has date as a key and price as a value
    dic = dict()
    for value_dict in result:
        dic[value_dict['date']]=float(value_dict['price'])

    dic = {k:v for (k,v) in dic.items() if k > year_day}

    latest_price= list(dic.values())[-1] 
    latest_date = list(dic.keys())[-1]
    print('Latest {0} {1:5.2f} {2}'.format(latest_date,latest_price,sym))
    rickon['z_Today'] = latest_date
    rickon['latest_price'] = latest_price
    j=0
    for bran in some_day:
        try:
            price_at_date = dic[bran]
            flag = ''
        except KeyError:
            flag = 'NA'
            price_at_date = list(dic.values())[0]

        delta_at_date = (latest_price/price_at_date-1)*100 
        #print('Gain from {1} {0:5.1f}% {2}'.format(delta_at_date,bran,flag))

        ix = str(list_day[j]) + "day"
        rickon[ix] = delta_at_date
        j=j+1


    set_day = '2018-02-13'
    try:
        price_at_date = dic[set_day]
        flag = ''
    except KeyError:
        flag = 'NA'
        price_at_date = list(dic.values())[0]
    delta_at_date = (latest_price/price_at_date-1)*100 
    #print('Gain from {1} {0:5.1f}% {2}'.format(delta_at_date,set_day,flag))
    rickon[set_day] = price_at_date

    from_bot = (latest_price/price_at_date-1)*100 

    max_value = max(dic.values())  # maximum value
    max_keys = [k for k, v in dic.items() if v == max_value] 
    #print('Max {0:5.3f} Date {1}'.format(max_value, max_keys))
    rickon['Max'] = from_bot
    min_value = min(dic.values())  # maximum value
    min_keys = [k for k, v in dic.items() if v == min_value] 
    #print('Min {0:5.3f} Date {1}'.format(min_value, min_keys))
    rickon['Min'] = min_value

    mnx_ratio = (max_value/min_value-1)*100
    #print('Max/Min {0:5.1f}%'.format(mnx_ratio))
    rickon['MaxMin'] = mnx_ratio

    mx_change = (latest_price/max_value-1)*100
    #print('Max change  {0:5.1f}%'.format(mx_change))
    rickon['MaxChg'] = mx_change

    mn_change = (latest_price/min_value-1)*100
    #print('Min change  {0:5.1f}%'.format(mn_change))
    rickon['MinChg'] = mn_change
    jorah[sym]=rickon

    rickon['z_Max'] = list(max_keys)[0]
    rickon['z_Min'] = list(min_keys)[0]

    try:
        com = mydict[sym]
    except KeyError:
        com = ""
    rickon['z_Comment'] = com

#print(rickon,type(rickon))
#print(jorah,type(jorah))
#print(jorah.keys())
aa = jorah['AAPL']
#print(type(aa))
#print(aa.keys())

fx = open('analysis.csv','w')
print('Symbole', end=',',file=fx)
for gg in aa.keys():
    print(gg, end=',',file=fx)
print(',',file=fx)

#baelish = jorah['AAPL']
#print(baelish)
#baelish = jorah['AMZN']
#print(jorah)
for varys in sorted(jorah.keys()):
    baelish = jorah[varys]
    print('{0}'.format(varys), end=',',file=fx)
    #print(varys, end=',')
    kb = list(baelish.keys())
    #print('{0}'.format(baelish[kb[0]]), end=',',file=fx)
    #del kb[0]
    for ka in kb:
        m = re.search("z_",ka)
        if m:
            print('{0}'.format(baelish[ka]), end=',',file=fx)
        else:
            print('{0:5.2f}'.format(baelish[ka]),end=',',file=fx)
        #print(baelish[ka],end=',')

    print(',',file=fx)
    #print(',')
