import numpy as np
array = np.random.randint(1,10,size=4).reshape(2,2);

result_array = array*10

print result_array
print result_array[0][0],result_array[1][0],result_array[1][1]