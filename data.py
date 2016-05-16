import json 
import pandas as pd
from collections import Counter
import numpy as np

# f = open("RC_2015-01.txt", "r")
# i = 1
# for line in f:
# 	file = open("10000000.txt","a")
# 	file.write(line)
# 	if i == 10000000:
# 		break
# 	i += 1

table_raw = []
f = open("100000.txt")
for line in f:
	j = json.loads(line)
	table_raw.append([j["author"], j["body"], j["ups"], j["subreddit"]])
f.close()


subs = [i[3] for i in table_raw ]
subs_count = Counter(subs)
subs_dict = dict((k, v) for k, v in subs_count.items() if v >= 500)

# subreddit = []		#subreddits that have >=500 comments
# subreddit_num = []
# for k, v in subs_count.items():
# 	if v < 1000:
# 		del subs_count[k]
# 	else:
# 		subreddit.append(k)
# 		subreddit_num.append(v)
# print len(subreddit)	#23


# keep the comment in top subreddits
# i = len(table) - 1
# while i >= 0:
# 	if table[i][3] not in subreddit:
# 		table.pop(i)
# 	i -= 1
# print len(table)

authors = [i[0] for i in table_raw ]
authors_count = Counter(authors)
authors_dict = dict((k, v) for k, v in authors_count.items() if v >= 0)

# author = []			#authors who have >=10 comments
# comment_num = []
# for k, v in authors_count.items():
# 	if v < 10:
# 		del authors_count[k]
# 	else:
# 		author.append(k)
# 		comment_num.append(v)
# print len(author)	#262


# i = len(table) - 1
# while i >= 0:
# 	if i % 100 == 0:
# 		print i
# 	if table[i][0] not in author:
# 		table.pop(i)
# 	i -= 1
# print len(table)

table = []
for line in table_raw:
	if line[0] in authors_dict and line[3] in subs_dict:
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


author_subreddit_ups = np.zeros((len(author), len(subreddit)))
author_subreddit_num = np.zeros((len(author), len(subreddit)))
num = 0
for line in table:
	if(num % 1000) == 0:
		print num
	num += 1
	if (line[0] in author) and (line[3] in subreddit):
		i = author.index(line[0])
		j = subreddit.index(line[3])
		author_subreddit_ups[i][j] += line[2]
		author_subreddit_num[i][j] += 1

#print np.sum(author_subreddit_num)
author_subreddit_ups /= (author_subreddit_num + 1e-16)


###############
for i in range(0, len(subreddit)):
	sum_column = np.sum(author_subreddit_num[:,i])
	for j in range(0, len(author)):
		author_subreddit_num[j][i] /= sum_column

###############

score = np.zeros((len(table), 3))	#num, avg
for i in range(0, len(table)):
	if(i % 1000 == 0):
		print i
	x = author.index(table[i][0])
	y = subreddit.index(table[i][3])
	score[i][0] = author_subreddit_num[x][y] 
	score[i][1] = author_subreddit_ups[x][y]
	score[i][2] = table[i][2]

np.savetxt("/Users/apple/Desktop/result/author_subreddit_num.csv", author_subreddit_num)
np.savetxt("/Users/apple/Desktop/result/author_subreddit_ups.csv", author_subreddit_ups)

file = open("./result/table.txt", "a")
file.writelines(["%s\n" % item  for item in table])
file.close()

file = open("./result/author.txt", "a")
file.writelines(["%s\n" % item  for item in author])
file.close()

file = open("./result/subreddit.txt", "a")
file.writelines(["%s\n" % item  for item in subreddit])
file.close()

score = pd.DataFrame(score)
score.to_csv('./result/score.csv')

















