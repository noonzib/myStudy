import numpy as np

array = np.arange(8).reshape(2,4)
left,right = np.split(array, [2], axis=1)

print array
print array.shape
print left
print left.shape
print right
print right.shape
print right[1][1]