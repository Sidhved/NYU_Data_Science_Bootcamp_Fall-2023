import numpy as np

A = np.zeros(3, int)
print("A = \n", A, "\n")
B = np.ones(3, int)
print("B = \n", B, "\n")

C = np.stack([A, B])

print("C(vertical stack) = \n", C, "\n")

D = np.hstack([A, B])

print("D(horizontal stack) = \n", D, "\n")