import json 
import pandas as pd
from collections import Counter
import numpy as np
from numpy import *


table_raw = []
f = open("season_raw.csv")
for line in f:
	a = line.strip('\n').strip('\r').split(",")
	if a[1] != 'AskReddit':
		table_raw.append(a)
f.close()
print table_raw[0]
del table_raw[0]
print table_raw[0]
print len(table_raw)

subs = []
for i in table_raw:
	if i[1] not in subs:
		subs.append(i[1])

data = np.zeros((len(subs), 4))
i = 0
while i < len(table_raw):
	ii = i / 12
	j = 0
	while j < 12:
		jj = j / 3
		data[ii][jj] += int(table_raw[i][4])
		i += 1
		j += 1

#data = log(data / 100000)
data /= np.max(data)

data_csv = []
for i in range(0, len(subs)):
	data_csv.append([subs[i], data[i][0], data[i][1], data[i][2], data[i][3]])

data = pd.DataFrame(data_csv)
data.to_csv('season2015log.csv')
	

20
100
200
1000