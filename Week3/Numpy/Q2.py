import numpy as np

A = np.array([1, 3, 5, 7, 9])
B = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("A = \n", A, "\n")

print("B = \n", B, "\n")

print("The elements common to A and B are: \n", np.intersect1d(A, B), "\n")