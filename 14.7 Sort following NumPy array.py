#7: Sort following NumPy array
#Case 1: Sort array by the second row
#Case 2: Sort the array by the second column

import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

sampleArray1 = sampleArray[sampleArray[:,2].argsort()]

print (sampleArray1)

print ("\n")

sampleArray2 = sampleArray[sampleArray[2].argsort()]

print (sampleArray2)