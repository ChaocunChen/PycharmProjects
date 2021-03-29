from sklearn.cluster import KMeans
x_train=[[12,1,3,4],
        [12,1,3,9],
        [34,67,4,90],
        [1,2,3,6]]




x_test=[[5,5,6,8],
        [12,1,3,9],
        [4,68,45,6],
        [45,22,31,33]]
model= KMeans(n_clusters=4,random_state=0)
model.fit(x_train)
predicted = model.predict(x_test)
print(predicted)
