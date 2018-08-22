import json
import csv
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='AS0C1JP1LQY65GBK')
#data, meta_data = ts.get_batch_stock_quotes('MSFT,FB,AAPL')
f = open('xdb4.json')
config = json.load(f)
#config = {'NULL': [{'date': '2018-07-06', 'price': '100.00'}]}

#symbole = ['TSLA','AMAT','LRCX','AMD','INTC']
#symbole = ['NVDA','MU','QCOM','PI','XLNX']
#symbole = ['AVGO','QRVO','TXN','ADI','ADBE']
#symbole = ['MSFT','CRM','NOW','RHT','WDAY']
#symbole = ['WDAY','SPLK','DATA','MDB','VMW']
#symbole = ['CAT','ACN','DBX','TWLO']
#symbole = ['CSCO','ANET','GS','BAC','V']
#symbole = ['PYPL','SQ','JPM','BABA','BIDU']
#symbole = ['WB','SNAP','TWTR','SPOT']
#symbole = ['HD','MMM','GE','JNJ','NKE']
#symbole = ['DIS','UPS','UTX','UNP','DWDP']
#symbole = ['WMT','BA','GD','LLL','NOC']
#symbole = ['RTN','MRK','ABT','SHOP','JD']
#symbole = ['COST','TGT','XOM','ALGN']
#symbole = ['QQQ','SPY']
#symbole = ['KLAC','HAL','IQ','SBUX','CMG']
#symbole = ['ABT','AGN','AIG','APC','APD']
#symbole = ['AXP','BAX','C','CVS','CVX']
#symbole = ['CXO','DXC','EBAY','EL','EMR']
#symbole = ['EOG','EXPE','FDX','GILD','HDS']
#symbole = ['KO','LVS','PRU','SLB']

#symbole = ['STI','TJX','TXT','UAA','ULTA']
#symbole = ['UNH','UNP','URI','MA','PANW']
#symbole = ['CI','DVN','FDC','JNPR','WYNN']
#symbole = ['ALK','CELG','EA','GBX','MSG']
#symbole = ['MYL','ALB','AMGN','DNKN','JBLU']
#symbole = ['SCHW','SFIX','SHAK','SHAK','VZ']
#symbole = ['ATVI','MNST','BMY','DISCK','STOR']
#symbole = ['OXY']
#symbole = ['BX','KKR']
#symbole = ['SPSC','YEXT']
#symbole = ['HLT','IT']
#symbole = ['AMCX','UAL','FRAC','NBR']
#symbole = ['LITE','VIAV','OCLR','FNSR']
#symbole = ['BP','CMCSA','DHR','HON']
#symbole = ['ITW','JWN','KSS','NUE']
symbole = ['PEP','WRK','XEC']

for sym in symbole:
    data, meta_data = ts.get_daily(sym,outputsize='full')
    keys = sorted(data.keys())
    dic = {}

    for item in keys:
        value = data[item]['4. close']
        dic[item] = value

    #d = {"symbole":sym, "daily":[{'date':key,'price':value} for key,value in dic.items()]}
    #d = {sym:[{'date':key,'price':value} for key,value in dic.items()]}
    d = [{'date':key,'price':value} for key,value in dic.items()]
    config[sym]=d

fx = open('xdb4.json','w')
fx.write(json.dumps(config))

