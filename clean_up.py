import json
import re


jsondata = json.load(open("xdb_temp.json"))
symbole = list(jsondata.keys())

for sym in symbole:
    result = dict()
    result = jsondata[sym]
    myData_clean = [x for x in jsondata[sym] if  re.search(r'20(20|21|22)-\d\d-\d\d', x['date']) ]
    #print(myData_clean)
    jsondata[sym]=myData_clean

fx = open('xdb_clean.json','w')
fx.write(json.dumps(jsondata))


