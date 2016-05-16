import json 
import pandas as pd
from collections import Counter
import numpy as np
import re
import itertools
from nltk.corpus import stopwords

"""
table_raw = []
f = open("1000000.txt")
for line in f:
	j = json.loads(line)
	table_raw.append([j["author"], re.sub("[^\w]", " ", j["body"]).split(), j["ups"], j["subreddit"]])
f.close()
# print table_raw[0]

subs = [i[3] for i in table_raw ]
subs_count = Counter(subs)
subs_dict = dict((k, v) for k, v in subs_count.items() if v >= 100)

authors = [i[0] for i in table_raw ]
authors_count = Counter(authors)
authors_dict = dict((k, v) for k, v in authors_count.items() if v >= 20)

table = []
for line in table_raw:
	if line[0] in authors_dict and line[0] != '[deleted]' and line[3] in subs_dict:
		table.append(line)

subs = [i[3] for i in table ]
subs_count = Counter(subs)
subreddit = subs_count.keys()
print "subreddit", len(subreddit)

authors = [i[0] for i in table ]
authors_count = Counter(authors)
author = authors_count.keys()

print authors_count


print "author", len(author)
print "table", len(table)


author_subreddit_num = np.zeros((len(author), len(subreddit)))
author_subreddit = np.zeros((len(author), len(subreddit)))
num = 0
for line in table:
	if(num % 1000) == 0:
		print num
	num += 1
	if (line[0] in author) and (line[3] in subreddit):
		i = author.index(line[0])
		j = subreddit.index(line[3])
		author_subreddit[i][j] = 1
		author_subreddit_num[i][j] += 1

for i in range(0, len(author)):
	if np.sum(author_subreddit[i]) > 3 and np.sum(author_subreddit_num[i]) > 40:
		print author[i]
		sub1 = [j[3] for j in table if j[0] == author[i]]
		sub1_count = Counter(sub1)
		sub1_dict = dict((k, v) for k, v in sub1_count.items() if v >= 0)
		dict1= sorted(sub1_dict.iteritems(), key=lambda d:d[1], reverse = True)
		print dict1[:10]
"""


table_raw = []
f = open("100000.txt")
for line in f:
	j = json.loads(line)
	table_raw.append([j["author"], re.sub("[^\w]", " ", j["body"]).split(), j["ups"], j["subreddit"]])
f.close()
# print table_raw[0]

subs = [i[3] for i in table_raw ]
subs_count = Counter(subs)
subs_dict = dict((k, v) for k, v in subs_count.items() if v >= 500)

# authors = [i[0] for i in table_raw ]
# authors_count = Counter(authors)
# authors_dict = dict((k, v) for k, v in authors_count.items() if v >= 10)

table = []
for line in table_raw:
	if line[0] != '[deleted]' and line[3] in subs_dict and line[3] != 'AskReddit':
		table.append(line)

stop_words = set(stopwords.words("english"))
remove = ['1','2','3','4','5','6','7','8','9','0','would','http','said','people','could','going','like','back','even','never','even','better','work','also','years']

words = [i[1] for i in table]
total_words = list(itertools.chain(*words))
total_words_count = Counter(total_words)
word_list = dict((k,v) for k,v in total_words_count.items() if v > 300)
word_list2 = sorted(word_list.keys())
word_list2 = [w for w in word_list2 if w.lower() not in stop_words]
word_list2 = [w for w in word_list2 if w not in remove and len(w) > 3]

print len(word_list)  # 26
print len(total_words_count)  # 5729
print word_list

data = []
for line in table:
	for word in line[1]:
		if word in word_list2:
			data.append([line[3], word])


data_csv = pd.DataFrame(data)
data_csv.to_csv('data2.csv')






# 500, 20
# subreddit 19
# author 68
# table 1855
"""
table_raw = []
f = open("1000000.txt")
for line in f:
	j = json.loads(line)
	table_raw.append([j["author"], j["body"], j["ups"], j["subreddit"]])
f.close()


subs = [i[3] for i in table_raw ]
subs_count = Counter(subs)
subs_dict = dict((k, v) for k, v in subs_count.items() if v >= 4000)
print subs_dict.keys()

table1 = []
for line in table_raw:
	if line[0] != '[deleted]' and line[3] in subs_dict:
		table1.append(line)

# authors = []
# for line in table1:
# 	if line[3] == 'nba':
# 		authors.append(line[0])
authors = [i[0] for i in table1]
authors_count = Counter(authors)
authors_dict = dict((k, v) for k, v in authors_count.items() if v >= 50)

print authors_dict

table = []
for line in table_raw:
	if line[0] in authors_dict and line[0] != '[deleted]' and line[3] in subs_dict:
		table.append(line)

subs = [i[3] for i in table ]
subs_count = Counter(subs)
subreddit = subs_count.keys()
#print subreddit
print "subreddit", len(subreddit)

authors = [i[0] for i in table ]
authors_count = Counter(authors)
author = authors_count.keys()
#print author
print "author", len(author)

print "table", len(table)

data = []
for line in table:
	data.append([line[3], line[0]])

data_csv = pd.DataFrame(data)
data_csv.to_csv('data.csv')
"""
