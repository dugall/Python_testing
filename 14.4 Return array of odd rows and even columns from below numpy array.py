#4: Return array of odd rows and even columns from below numpy array
import numpy as np

sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24],
	[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])


print (sampleArray)
print ("\n")
print (sampleArray[::2])
print ("\n")
print (sampleArray[:, 1::2])

#https://stackoverflow.com/questions/10198747/how-can-i-simultaneously-select-all-odd-rows-and-all-even-columns-of-an-array