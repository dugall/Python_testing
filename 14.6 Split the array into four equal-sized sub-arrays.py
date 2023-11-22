#6: Split the array into four equal-sized sub-arrays
#Note: Create an 8X3 integer array from a range between 10 to 34 such that
#the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.

import numpy as np

sampleArray = np.array(range(10,34))
sampleArray = sampleArray.reshape(8,3)

print (sampleArray)
print ("\n")

newarray = sampleArray.reshape(4,2,3)

print (newarray)


newarray1 = np.split(sampleArray, 4)

print (newarray1)