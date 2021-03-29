from sklearn import tree
from skimage import data
# x_train = data.load('/Users/chenchaocun/Downloads/JPG/JPG/IMG_2752.jpg')
# print(x_train.shape)
# y_train = data.load('/Users/chenchaocun/Downloads/JPG/JPG/IMG_2744.jpg')
# x_test = data.load('/Users/chenchaocun/Downloads/JPG/JPG/IMG_2740.jpg')

x_train=[[12,1,3,4],
        [12,1,3,9],
        [34,67,4,90],
        [1,2,3,6]]


y_train=[[34,3,45,66],
        [67,78,90,30],
        [67,78,90,57],
        [90,4,22,90]]


x_test=[[5,5,6,8],
        [12,1,3,9],
        [4,68,45,6],
        [45,22,31,33]]

model = tree.DecisionTreeRegressor()
model.fit(x_train,y_train)
model.score(x_train,y_train)
predictted = model.predict(x_test)
print(predictted)