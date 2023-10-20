import numpy as np

# Create a numpy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Extract all numbers within the range of 5 to 10
result = np.where(np.logical_and(array >= 5, array<=10))

print(result)