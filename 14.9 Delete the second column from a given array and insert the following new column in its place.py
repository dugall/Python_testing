#9: Delete the second column from a given array and insert the following new column in its place.
import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
newColumn = np.array([[10,10,10]])

z = np.delete(sampleArray, [1], 1)
print(z)

y = np.insert(z, 1, newColumn, axis=1)

print (y)





