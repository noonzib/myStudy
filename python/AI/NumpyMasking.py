import numpy as np 

array1 = np.arange(16).reshape(4,4)
print array1

array2 = array1 < 10
print array2

array1[array2] = 100
print array1