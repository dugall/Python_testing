#8: Print max from axis 0 and min from axis 1 from the following 2-D array.

import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

max_value = np.max(sampleArray, axis = 0)

print (max_value)

min_value = np.min(sampleArray, axis = 1)

print (min_value)