# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:08:07 2016

"""

import json 
import pandas as pd
from collections import Counter
import re
import itertools
from pandas import DataFrame
import numpy as np

f = open('100000.txt')


table = []

a = 0

 
while a < 100000:
    line = f.readline()
    o = json.loads(line)
    #oo= [o["author"],re.sub("[^\w]", " ", o["body"]).split(),o["ups"],o["subreddit"]]
    oo = [re.sub("[^\w]", " ", o["body"]).split(), o["subreddit"], o["ups"],o["author"]]  
    table.append(oo)
    a+=1




names = [i[1] for i in table ]
names_count = Counter(names)
subre_dict = sorted(dict((k,v) for k,v in names_count.items() if v >= 500))


authors = [i[3] for i in table]
authors_count = Counter(authors)
authors_dict = dict((k,v) for k,v in authors_count.items() if v >= 0)


filtered_table = []
for line in table:
    if line[1] in subre_dict and line[3] in authors_dict:
        filtered_table.append(line)
for x in filtered_table:
    x.pop(3)
    

#filtered_table.insert(0,['body','subreddit', 'ups'])


words = [i[0] for i in filtered_table]
total_words = list(itertools.chain(*words))
total_words_count = Counter(total_words)
word_list = dict((k,v) for k,v in total_words_count.items() if v > 50)
word_list2 = sorted(word_list.keys())





ups_matr = np.zeros(shape=(len(word_list),len(subre_dict)))
count_matr = np.zeros(shape=(len(word_list),len(subre_dict)))

for x in range(0,len(filtered_table)):
    for y in filtered_table[x][0]:
        if y in word_list2:
            ups_matr[word_list2.index(y)][subre_dict.index(filtered_table[x][1])] += filtered_table[x][2]
            count_matr[word_list2.index(y)][subre_dict.index(filtered_table[x][1])] += 1
            
            
            
average_count = ups_matr/(count_matr+0.000000000001)        


ups_res = np.zeros(len(filtered_table))

subree = []
for x in range(len(filtered_table)):
    subree.append(filtered_table[x][1])
    if (x % 1000 == 0):
        print x
    line_ups = 0
    if filtered_table[x][1] in subre_dict:
        for y in filtered_table[x][0]:
            if y in word_list2:
                line_ups += average_count[word_list2.index(y)][subre_dict.index(filtered_table[x][1])]    #basically same as previous but sum ups instead of frequencies.
        line_ups = line_ups/(len(filtered_table[x][0])+0.0000000000001)        
        ups_res[x] = line_ups
    else:
        ups_res[x] = 0
    

#ups_res=pd.DataFrame(ups_res)
subree=pd.DataFrame(subree)
#ups_res.to_csv('word_ups.csv')
subree.to_csv('subree.csv')






