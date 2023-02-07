import re
import json
import datetime
from datetime import date
import calendar
import ast
import csv
from collections import OrderedDict

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

fc = open('C:\\Users\\jinc.SILVACOCORP.000\\OneDrive\\Script\\comment.csv')
reader = csv.reader(fc)
mydict = {}
name_dict ={}
for row in reader:
    mydict[row[0]] = row[1]
    #name_dict[row[0]] = row[2] 

fc = open('C:\\Users\\jinc.SILVACOCORP.000\\OneDrive\\Script\\record.csv')
reader = csv.reader(fc)
buy_dict = {}

for row in reader:
    key = row[0]
    if key in buy_dict:
       pass
    buy_dict[key] = row[1:]

fc = open('C:\\Users\\jinc.SILVACOCORP.000\\OneDrive\\Script\\dividend.csv')
reader = csv.reader(fc)
div_dict = {}
for row in reader:
    div_dict[row[0]] = row[1]


#print(buy_dict['AAPL'][0])

#
#
# read_json.py uses xdb3.json db
#
#
f = open('C:\\Users\\jinc.SILVACOCORP.000\\OneDrive\\Script\\xdb_temp.json')
data = json.load(f)
#print(data.keys())
symbole = list(data.keys())
#print(symbole)

aa=data['AAPL']
data_str = json.dumps(aa) 
d_year = 364
year_day=date_open(d_year,data_str)

list_day = [7,30,60,90,364]
some_day = list()
i=0;
for baelish in list_day:
    arya_day=date_open(baelish,data_str)
    some_day.append(arya_day)
    print(some_day)

#symbole = ['AAPL']

jorah = {}
key_dict = {}
for sym in symbole:
    rickon= OrderedDict()
    result = OrderedDict()
    day_price = OrderedDict()
    #print(sym)
    result = data[sym]
    #print(result)
    #dic is the new dictionary which has date as a key and price as a value
    dic = OrderedDict()
    owndic = {} 

    for value_dict in result:
        dic[value_dict['date']]=float(value_dict['price'])
    dic = {k:v for (k,v) in dic.items() if k > year_day}

    latest_price= list(dic.values())[-1] 
    latest_date = list(dic.keys())[-1]
    #print(list(dic.keys()))
    print('Latest {0} {1:5.2f} {2}'.format(latest_date,latest_price,sym))
    rickon['z_Today'] = latest_date
    #print(latest_date)
    rickon['latest_price'] = latest_price
    j=0
    for k in range(3):
        m = -2-k
        try:
            price_at_date = list(dic.values())[m] 
            at_date = list(dic.keys())[m] 
        except (ValueError,IndexError):
            price_at_date = list(dic.values())[0]
            at_date = list(dic.keys())[0] 
        delta_at_date = (latest_price/price_at_date-1)*100 
        ix = str(k+1) + "day"
        rickon[ix] = delta_at_date
        day_price[ix] = price_at_date
        #print(m,at_date,price_at_date)

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
        day_price[ix] = price_at_date
        j=j+1

    min_value = min(dic.values())  # maximum value
    min_keys = [k for k, v in dic.items() if v == min_value] 
    #print('Min {0:5.3f} Date {1}'.format(min_value, min_keys))
    #rickon['Min'] = min_value

    max_value = max(dic.values())  # maximum value
    max_keys = [k for k, v in dic.items() if v == max_value] 
    #print('Max {0:5.3f} Date {1}'.format(max_value, max_keys))

    mnx_ratio = (max_value/min_value-1)*100
    #print('Max/Min {0:5.1f}%'.format(mnx_ratio))
    #rickon['MaxMin'] = mnx_ratio

    mx_change = (latest_price/max_value-1)*100
    #print('Max change  {0:5.1f}%'.format(mx_change))

    mn_change = (latest_price/min_value-1)*100
    #print('Min change  {0:5.1f}%'.format(mn_change))

    #aaa = rickon['7day'] - rickon['3day']
    #bbb = rickon['7day'] - rickon['2day']
    #if aaa < bbb:
    #    rickon['Dip'] = aaa
    #else:
    #    rickon['Dip'] = bbb 

    rickon['frMin'] = float("{0:.1f}".format(mn_change))
    rickon['frMax'] = float("{0:.1f}".format(mx_change))
    rickon['Max'] = max_value

    set_day = '2022-10-12'
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

    rickon['FrBot'] = from_bot


    x_range = max_value/price_at_date 
    #rickon['range'] = x_range
    
    x_ideal = x_range*8.1+0.31
    x_dev = from_bot-x_ideal
    #rickon['relative'] = x_dev

    rickon['z_sym'] = sym

    try:
        com = round((latest_price-float(buy_dict[sym][1]))/float(buy_dict[sym][1])*100,2)
    except KeyError:
        com = ""
    rickon['z_perf'] = com

    try:
        com = buy_dict[sym][0]
        for value_dict in result:
            owndic[value_dict['date']]=float(value_dict['price'])
        owndic = {k:v for (k,v) in dic.items() if k > com}
        try:
            max_own = max(owndic.values())  # maximum value
        except:
            max_own = latest_price
    except KeyError:
        com = ""
    zdate = com

    if com == "":
        xx = ""
    else:
        xx = (latest_price/max_own-1)*100

    rickon['fr_high'] = xx 

    try:
        com = float(buy_dict[sym][2])*(latest_price-float(day_price['1day']))
    except (ValueError,KeyError,IndexError):
        com = ""
    rickon['d_profit'] = com

    try:
        com = float(buy_dict[sym][2])*(latest_price-float(buy_dict[sym][1]))
    except (ValueError,KeyError,IndexError):
        com = ""
    rickon['t_profit'] = com

    try:
        com = float(buy_dict[sym][1])
    except KeyError:
        com = ""
    rickon['b_price'] = com

    try:
        com = float(buy_dict[sym][2])*latest_price
    except KeyError:
        com = ""
    rickon['mk_value'] = com

    try:
        com = float(buy_dict[sym][2])
    except (ValueError,KeyError,IndexError):
        com = ""
    rickon['n_sh'] = com 
  

##
## Buying analysis
##
    try:
        com = mydict[sym]
    except KeyError:
        com = ""
    rickon['z_setP'] = com

    vin = (latest_price - float(com or 0))/latest_price ; 

    try:
        com = vin
    except KeyError:
        com = ""
    if vin == 1: com = ""
    rickon['z_Sig'] = com

#    try:
#        ccc = name_dict[sym] 
#    except KeyError:
#        ccc = ""
#    rickon['z_Name'] = ccc
    
##
## Dividend analysis
##
    try:
        com = div_dict[sym]
    except KeyError:
        com = ""
    rickon['z_divQ'] = com

    vin = (latest_price - float(com or 0))/latest_price ; 

    try:
        com = vin
    except KeyError:
        com = ""
    if vin == 1: com = ""
    rickon['z_divY'] = com

   
    jorah[sym]=rickon

#print(rickon,type(rickon))
#print(jorah,type(jorah))
#print(jorah.keys())
bb = jorah['AAPL']
#print(bb)
  
fx = open('C:\\Users\\jinc.SILVACOCORP.000\\OneDrive\\Script\\analysis.csv','w')
print('Symbole', end=',',file=fx)
for gg in bb.keys():
    print(gg, end=',',file=fx)
print(',',file=fx)




#baelish = jorah['AAPL']
#print(baelish)
#baelish = jorah['AMZN']
#print(jorah)
for varys in sorted(jorah.keys()):
#for varys in jorah.keys():
    baelish = jorah[varys]
    print('{0}'.format(varys), end=',',file=fx)
    #print(varys, end=',')
    kb = list(baelish.keys())
    #print('{0}'.format(baelish[kb[0]]), end=',',file=fx)
    #del kb[0]
    for ka in kb:
        m = re.search("_",ka)
        if m:
            print('{0}'.format(baelish[ka]), end=',',file=fx)
        else:
            print('{0:5.2f}'.format(baelish[ka]),end=',',file=fx)
        #print(baelish[ka],end=',')

    print(',',file=fx)
    #print(',')

print(len(symbole))
