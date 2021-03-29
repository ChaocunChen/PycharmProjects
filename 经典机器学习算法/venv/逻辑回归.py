#coding=utf-8
from sklearn.linear_model import LogisticRegression
from skimage import data
import numpy as np
#y_train 必须一维
x_train=[[12,1,3,4],
        [12,1,3,9],
        [34,67,4,90],
        [1,2,3,6]]


y_train= [67,78,90,30]



x_test=[[5,5,6,8],
        [12,1,3,9],
        [4,68,45,6],
        [45,22,31,33]]
print(np.array(x_train).shape)
print(len(x_train))
model = LogisticRegression()
model.fit(x_train,y_train)
model.score(x_train,y_train)
print('score={}'.format(model.coef_))
print('Intercep={}'.format(model.intercept_))
predicted = model.predict(x_test)