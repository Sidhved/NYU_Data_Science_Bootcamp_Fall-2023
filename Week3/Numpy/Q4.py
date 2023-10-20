import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

res = np.where(np.logical_and(iris_2d[:, 2]<1.5, iris_2d[:, 0]>5))

print(iris_2d[res])