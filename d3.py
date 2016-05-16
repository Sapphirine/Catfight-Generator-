import json 
import pandas as pd
from collections import Counter
import numpy as np

# subreddit 156
# author 13791
# table 276640

author_subreddit_num = np.loadtxt("/Users/apple/Desktop/result/author_subreddit_num.csv")
#print np.shape(author_subreddit_num)  #(13791, 156)

author = []
f = open('/Users/apple/desktop/result/author.txt')
line = f.readline()
while line:
	author.append(line.strip('\n'))
	line = f.readline()
f.close()

result = []
for i in range(0, 13791):
	for j in range(0, 156):
		if author_subreddit_num[i][j] > 0:
			author_subreddit_num[i][j] = 1
		else:
			author_subreddit_num[i][j] = 0
	if np.sum(author_subreddit_num[i]) > 10:
		a = []
		a.append(author[i])
		tmp = 0
		for j in range(0, 156):
			if author_subreddit_num[i][j] > 0:
				a.append(1)
				tmp += 1
			else:
				a.append(0)
		a.append(tmp)
		result.append(a)


subreddit = []
subreddit.append('username')
f = open('/Users/apple/desktop/result/subreddit.txt')
line = f.readline()            
while line:
	subreddit.append(line.strip('\n'))
	line = f.readline()
f.close()

subreddit.append('total')

# result.insert(0, subreddit)

result_pd = pd.DataFrame(result, columns = subreddit)
result_pd.to_csv('./result/d3_result2.csv')
