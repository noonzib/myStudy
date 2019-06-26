import numpy as np 

array = np.arange(16).reshape(4,4)

print array
print("SUM:",np.sum(array, axis=0))