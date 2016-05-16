# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

 
while a < 1000000:
    line = f.readline()
    o = json.loads(line)
    #oo= [o["author"],re.sub("[^\w]", " ", o["body"]).split(),o["ups"],o["subreddit"]]
    oo = [re.sub("[^\w]", " ", o["body"]).split(), o["subreddit"],o["author"]]       #sprate body content
    table.append(oo)
    a+=1



names = [i[1] for i in table ]
names_count = Counter(names)
subre_dict = dict((k,v) for k,v in names_count.items() if v >= 1000)       #pick subreddit that shows at least 1000 times

authors = [i[2] for i in table]
authors_count = Counter(authors)
authors_dict = dict((k,v) for k,v in authors_count.items() if v >= 10)     #pick author who posts at least 10 times

filtered_table = []
for line in table:
    if line[1] in subre_dict and line[2] in authors_dict:
        filtered_table.append(line)
for x in filtered_table:                                                   #append the satisfied lines to filtered_table, remove author column
    x.pop(2)

names = [i[1] for i in filtered_table ]                                     #find all subreddit 
subre_dict = Counter(names)
   
   
   
#filtered_table.insert(0,['body','subreddit' ])



words = [i[0] for i in filtered_table]
total_words = list(itertools.chain(*words))
total_words_count = Counter(total_words)
word_list = dict((k,v) for k,v in total_words_count.items() if v > 50)          #pick words that show up more than 50 times
word_list2 = sorted(word_list.keys())


subre_dict2 = sorted(subre_dict)

print 'subreddit len',len(subre_dict2)
print 'word list len',len(word_list2)
'''
for x in range(1,len(filtered_table)):
    y = filtered_table[x][0]
    for z in y:
        zz = str(z)
        if zz not in word_list:
            filtered_table[x][0].remove(z)
'''


####topic{author{sum of score}}

print 'capstone 1'
        
        
'''        
df = DataFrame(filtered_table, columns = filtered_table[0]) 


df['merge'] = df.apply(lambda row: df.groupby('subreddit').get_group(row['subreddit'])['body'].tolist(), axis=1)
df.drop_duplicates(subset=['subreddit'],inplace = True)



df.index=range(len(df))
for x in range(len(df['body'])):
    df['merge'][x] = list(itertools.chain(*df['merge'][x]))
    df['merge'][x] = Counter(df['merge'][x])
'''    

df= []
for x in range(len(subre_dict2)):                                       #create a list for each subreddit to store words
    df.append([])

for x in range(0,len(filtered_table)):                                  #append words in each line to each list under each subreddit
    for y in filtered_table[x][0]:
        if y in word_list2:
            df[subre_dict2.index(filtered_table[x][1])].append(y)
            
for x in range(len(df)):
    df[x]= Counter(df[x])

df_sum=[]
for x in range(len(df)):
    df_sum.append(sum(df[x].values()))


    
print 'capstone2'
    
#word_counted = lambda x: Counter(x)
#df['merge'] = df['merge'].map(word_counted)




final_matr = np.zeros(shape=(len(word_list2),len(subre_dict2)))
for x in range(len(word_list2)):                                      #put word count result from each dictionary from each subreddit
    print x
    for y in range(0,len(subre_dict2)):
        if word_list2[x] in df[y]:
            final_matr[x][y] =  float(df[y][word_list2[x]])/df_sum[y]
            
            
freq_res = np.zeros(len(filtered_table))

for x in range(len(filtered_table)):
    if (x % 1000 == 0):
        print x
    line_ups = 0
    if filtered_table[x][1] in subre_dict2:
        for y in filtered_table[x][0]:
            if y in word_list2:
                line_ups += final_matr[word_list2.index(y)][subre_dict2.index(filtered_table[x][1])]     #scan filtered lines, calculate average words frequency score for the line by sum up words frequencies and divide by lenght of body. 
        line_ups = line_ups/(len(filtered_table[x][0])+0.0000000000001)       
        freq_res[x] = line_ups
    else:
        freq_res[x] = 0

#freq_res = np.delete(freq_res, 0)    
freq_res=pd.DataFrame(freq_res)

freq_res.to_csv('word_freq.csv')



word_list_res = pd.DataFrame(word_list2)    
word_list_res.to_csv('word_list.csv')    
    
    
    
    
##########################################################################


















