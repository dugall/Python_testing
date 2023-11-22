#10: Create two 2-D arrays and Plot them using matplotlib

import numpy as np
import matplotlib.pyplot as plt

sampleArray1 = np.array([[12,12,12],[82,22,12],[53,94,66]]) 
sampleArray2 = np.array([[34,43,73],[345,34,1212],[53,94,66]]) 

#plt.scatter(sampleArray1[:, 0], sampleArray1[:, 1], c=sampleArray1[:, 2], cmap='hot')
plt.plot(sampleArray1)
plt.show()

plt.plot(sampleArray2)
plt.show()

# Set the figure size
#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True

# Random data of 100×3 dimension
#data = np.array(np.random.random((100, 3)))

# Scatter plot
#plt.scatter(data[:, 0], data[:, 1], c=data[:, 2], cmap='hot')

# Display the plot
#plt.show()