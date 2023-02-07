import math
import pylab
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import re
import json
import datetime
from datetime import date
import calendar
import csv
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import matplotlib.dates as mdates
from numpy import arange
from matplotlib.legend_handler import HandlerLine2D

def computeTicks (x, step = 10):
    """
    Computes domain with given step encompassing series x
    @ params
    x    - Required - A list-like object of integers or floats
    step - Optional - Tick frequency
    """
    import math as Math
    xMax, xMin = Math.ceil(max(x)), Math.floor(min(x))
    dMax, dMin = xMax + abs((xMax % step) - step) + (step if (xMax % step != 0) else 0), xMin - abs((xMin % step))
    return range(dMin, dMax, step)


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
        print('{0} days from today is {1} {2}'.format(days_ago,sd,calendar.day_name[sd.weekday()]))
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

def indices(l, val):
    return [index for index, value in enumerate(l) if value == val]


header = pd.read_csv("analysis.csv",nrows=1).columns
list_header = header.tolist()



df1 = pd.read_csv("analysis.csv")
# This is the way to convert to panda db to numpy matrix
numpy_matrix = df1.values


head_name = ['7day','30day','60day','90day','364day']
index_all = []
for bx in head_name:
    index_all.append(indices(list_header,bx)[0])

#print(index_all)

my =[]
with open('record.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        my.append(row[0]) 

print(my)

chart_type = input('Type my/0,10,20,30,40,50: ')
chart_range = int(input('Type 7,30,60,90,364: '))

ix = str(chart_range)+'day'
l_index = indices(list_header,ix)


#input_dict = {5:4,30:5,60:6,90:7,120:8,364:9}
sixty = np.array(numpy_matrix[:,l_index[0]])
ticket = numpy_matrix[:,0]
sixty_idx = np.argsort(-sixty)
tick = numpy_matrix[:,0]
#print(sixty)
#print(ticket)
#print(sixty_idx)
#exit()

if chart_type == 'my':
    rng = len(my)
    symbole =[]
else:
    my = ['SPY']
    symbole =['SPY']
    rng = 10
    st = int(chart_type)
    for i in range(rng):
        #print(ticket[sixty_idx[i]])
        j = i + st 
        my.append(ticket[sixty_idx[j]])


ref_sym = ['SPY']
ref_dic = dict()
for cmp in index_all:
    tx_idx = np.where(tick == ref_sym[0])
    tt = list(tx_idx[0])[0]
    ref = numpy_matrix[:,cmp]
    ref_dic[cmp] = ref[tt]

#print(ref_dic)

for sm in my:
    main_dic = dict()
    mail_list = []
    for cmp in index_all:
        tx_idx = np.where(tick == sm)
        tt = list(tx_idx[0])[0]
        main = numpy_matrix[:,cmp]
        #main_dic[cmp] = main[tt]-ref_dic[cmp]
        main_dic[cmp] = main[tt]

    main_list = list(main_dic.values())
    zx = list(map(lambda n: "%.2f" % n, main_list))
    z = list(map(float,zx))
    print(sm,z)
   


plt.gca().legend(my)
#plt.xticks(computeTicks(x), rotation = 'vertical')
#plt.show()


### This is a graphic module ##

six = np.array(numpy_matrix[:,l_index])

ticket=np.array([])
sixty=np.array([])
tx_idx = dict() 
idx_list = []
for tx in my:
    tx_idx = np.where(tick == tx)
    tt = list(tx_idx[0])[0]
    idx_list.append(tt)
    ticket=np.append(ticket,tick[tt])
    sixty =np.append(sixty,six[tt])

sixty_idx = np.argsort(-sixty)

#for idx in sixty_idx:
    #print(ticket[idx], sixty[idx])

f = open('xdb_temp.json')
data = json.load(f)

aa=data['SPY']
data_str = json.dumps(aa)
some_day = date_open(chart_range+1,data_str)
#print(some_day)
#exit()

for i in range(rng):
    #print(ticket[sixty_idx[i]])
    symbole.append(ticket[sixty_idx[i]])

jorah = {}
theon =dict()
for sym in symbole:
    rickon=dict()
    result = dict()
    #print(sym)
    result = data[sym]
    #dic is the new dictionary which has date as a key and price as a value
    dic = dict()
    for value_dict in result:
        dic[value_dict['date']]=float(value_dict['price'])

    dic = {k:v for (k,v) in dic.items() if k > some_day}
    theon[sym]=list(dic.values())

#print(theon[sym])

y = list(dic.values())
x = range(len(y)) 
labels = list(dic.keys())

#f2 = plt.figure(2)
for sym in symbole:
    start = list(theon[sym])[0]
    #print(start)
    y = [ (i/start-1)*100 for i in theon[sym]]
    plt.plot(x,y,marker='*')

plt.gca().legend(symbole)

#plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)}
#plt.xticks(x, labels , rotation = 'vertical')
plt.xticks(computeTicks(x), rotation = 'vertical')

plt.show()
