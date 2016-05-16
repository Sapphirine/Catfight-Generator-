import json 
import pandas as pd
from collections import Counter
import numpy as np
import re
import itertools
from nltk.corpus import stopwords

table_raw = []
f = open("1000000.txt")
for line in f:
	j = json.loads(line)
	table_raw.append([j["ups"], j["subreddit"]])
f.close()

score = []
subs = ['serialpodcast','GlobalOffensive','leagueoflegends','news','nfl','CFB','pics','movies','AskReddit','DotA2']
score.append(subs)
for i in table_raw:
	if i[1] in subs:
		tmp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		index = subs.index(i[1])
		tmp[index] = i[0]
		score.append(tmp)

score_csv = pd.DataFrame(score)
score_csv.to_csv('circulus.csv')

