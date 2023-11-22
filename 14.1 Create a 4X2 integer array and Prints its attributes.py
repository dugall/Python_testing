#1: Create a 4X2 integer array and Prints its attributes
#Expected Output:
#Printing Array
#[[64392 31655]
# [32579     0]
# [49248   462]
# [    0     0]]
#Printing NumPy array Attributes
#Array Shape is:  (4, 2)
#Array dimensions are  2
#Length of each element of array in bytes is  2

import numpy as np

array1 = np.array([[64392, 31655], [32579,    0 ], [49248,   462], [    0,     0]])

print ("Printing array", "\n")
print (array1, "\n")
print ("Printing NumPy array Attributes\n")
print ("Array Shape is:", array1.shape)
print ("Array dimensions are", array1.ndim)
print ("Length of each element of array in bytes is", len(array1))

