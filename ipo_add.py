
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

f = open('single.json')
jdata = json.load(f)
df = pd.DataFrame(jdata)
df['price']="186"
print(df)
result = df.to_json(orient="records")
print(result)
fx = open('xdb_single.json','w')
fx.write(result)
