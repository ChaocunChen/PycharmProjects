from sklearn.ensemble import RandomForestClassifier

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

model=RandomForestClassifier()
model.fit(x_train,y_train)
predicted=model.predict(x_test)
print(predicted)