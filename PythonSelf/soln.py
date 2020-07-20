import numpy as np

X_train=np.array([[5,4], [4,5], [4,4], [6,-6]])

class MyKNN:
    def __init__(self, k):
        self.k = k

    def Build_KDTree(self, data, depth = 0):
        n = len(data)
        return n

knn = MyKNN(3)
knn.Build_KDTree(X_train)
