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

f = open('C:\\Users\\hyunj\\OneDrive\\Script\\xdb_temp.json')
data = json.load(f)
#print(data.keys())
symbole = list(data.keys())
#print(symbole)

aa=data['AMZN']
data_str = json.dumps(aa) 
print(data_str)
