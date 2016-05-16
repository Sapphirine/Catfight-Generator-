# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:15:52 2016

@author: panpan
"""
import pandas as pd
import numpy
import statsmodels.api as sm
from pandas.stats.api import ols
from sklearn.pipeline import *
from sklearn.preprocessing import *
from sklearn import *
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsRegressor
import difflib
from sklearn.qda import QDA
from sklearn.lda import LDA
import numpy as np


data  = pd.read_csv('score.csv')
data1 = pd.read_csv('word_freq.csv')
data2 = pd.read_csv('word_ups.csv')

data['3'] = pd.DataFrame(data1['0'])
data['4'] = pd.DataFrame(data2['0'])
data=data.drop(data.columns[[0]],axis=1)
#data=data.drop(data.columns[[1]],axis=1)
#data['1'] = np.power(data['1'], 3)


y = pd.DataFrame(data['2'])
data=data.drop(data.columns[[2]],axis=1)
np_data = numpy.array(data)
np_y = numpy.array(y)

l = np_data.shape[0]
#Data = numpy.hstack((numpy.ones((l,1)),np_data))
data = pd.DataFrame(data)
poly = PolynomialFeatures(2)
data =poly.fit_transform(data)



model = sm.OLS(y,data)
results = model.fit()
results.summary()


data = pd.DataFrame(data)                   #drop nonsignificant column
data = data.drop(data.columns[[10,5,7,12,14]],axis=1)
data = np.array(data)

model = sm.OLS(y,data)
results = model.fit()
results.summary()
#re = results.t_test([4,3,2,1,0])


## qqpolt
#z = np.polyfit(Data, y, 2)
mod_fit = sm.OLS(y,data).fit()
res = mod_fit.resid
fig = sm.qqplot(res)
#plt.show()




#################


average_score = []                  #knn result
for k in [5, 10,50,100,150,200, 1000]:
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(data, y, test_size=0.05, random_state=0)
    neigh = KNeighborsRegressor(n_neighbors=k)
    neigh.fit(X_train, y_train)
    average_score.append(neigh.score(X_test,y_test))
    
  

#Comparatively k = 10 is best  
X_train, X_test, y_train, y_test = cross_validation.train_test_split(data, y, test_size=0.05, random_state=0)
neigh = KNeighborsRegressor(n_neighbors=10)
neigh.fit(X_train, y_train)
predict_result1 = neigh.predict(data)




#############################classification

subre_list = ['videos', 'todayilearned', 'nba','funny', 'DestinyTheGame', 'AdviceAnimals','hockey','WTF', 'worldnews','pcmasterrace','soccer','anime','gaming','serialpodcast','GlobalOffensive','leagueoflegends','news','nfl','CFB','pics','movies','AskReddit','DotA2']
bar = [13,17,19,11,5,13,7,13,10,3,14,9,9,10,3,7,9,22,9,10,11,5,5]

subree_bar = pd.read_csv('subree.csv')
subree_bar.columns = ['a', 'b']
subree_bar = subree_bar.drop(['a'],axis=1)
subreee = subree_bar['b'].tolist()

top_comments = []
for x in range(len(y)):
    if y[x] > bar[subre_list.index(subreee[x])]:
        top_comments.append(x)





# logistic
class_y = []
one_position = []
for x in range(len(y)):
    if y['2'][x] > bar[subre_list.index(subreee[x])]:
        class_y.append(1)
        one_position.append(x)
    else:
        class_y.append(0)
      


X_train2, X_test2, y_train2, y_test2 = cross_validation.train_test_split(data, class_y, test_size=0.05, random_state=0)
logreg = linear_model.LogisticRegression()
logreg.fit(X_train2, y_train2)
logreg.score(X_test2,y_test2)
predict_result2 = logreg.predict(X_test2)

sum(predict_result2)
sm = difflib.SequenceMatcher(None, predict_result2, y_test2)
sm.ratio()



X_train2 = np.array(X_train2)
X_test2 = np.array(X_test2)
y_train2 = np.array(y_train2)
y_test2 = np.array(y_test2)
clf = LDA()
clf.fit(X_train2, y_train2)
clf.score(X_test2, y_test2)








# bing graph
sub_list = ['serialpodcast','GlobalOffensive','leagueoflegends','news','nfl','CFB','pics','movies','AskReddit','DotA2']

li = []
for i in range(0, len(sub_list)):
    li.append([])

for x in range(len(y)):
    if subreee[x] in sub_list:
        sub_list.index(subreee([x]))
        

'''
