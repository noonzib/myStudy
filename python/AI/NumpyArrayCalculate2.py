import numpy as np 
array1 = np.arange(4).reshape(4, 1) 
array2 = np.arange(4) 
array3 = array1 + array2 
print array1
print array2
print(array3[0][0], array3[0][1], array3[0][2], array3[0][3]) 
print(array3[1][0], array3[1][1], array3[1][2], array3[1][3])
print(array3[2][0], array3[2][1], array3[2][2], array3[2][3]) 
print(array3[3][0], array3[3][1], array3[3][2], array3[3][3])
