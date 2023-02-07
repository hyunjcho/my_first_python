
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

input_file = "C:\\Users\\jinc.SILVACOCORP.000\\Downloads\\quotes.csv"
try:
    f = open(input_file)
    s = f.readline()
except OSError as err:
    print("There is no quotes.csv!!")
    print("Please export file from YAHOO!")
    exit()

dfx = pd.read_csv(input_file)
df = dfx.iloc[:,:4].replace(regex={'/':'-'})


f = open('C:\\Users\\jinc.SILVACOCORP.000\\OneDrive\\Script\\xdb_main.json')
fx = open('C:\\Users\\jinc.SILVACOCORP.000\\OneDrive\\Script\\xdb_temp.json','w')
org = json.load(f)
symbole = list(org.keys())
print(symbole)

mydict = {}
for sym in symbole:
    df_xx = df[df['Symbol']==sym]
    price = df_xx['Current Price'].values[0]
    date =  df_xx['Date'].values[0]
    s = {'date': date, 'price': price}
    org[sym].append(s)
    #print(sym,date,price)

fx.write(json.dumps(org))
#print(len(symbole))
#os.remove(input_file)
#subprocess.call("C:\\Users\\hyunj\\OneDrive\\Script\\remove.bat")
