import numpy as np

array = np.empty((0,3), int)

array = np.append(array, np.array([[1,3,5]]), axis=0)
array = np.append(array, np.array([[2,4,6]]), axis=0)

print(array)