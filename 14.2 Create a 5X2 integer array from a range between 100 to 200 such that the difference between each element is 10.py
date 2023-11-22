#2: Create a 5X2 integer array from a range between 100 to 200
#such that the difference between each element is 10

import numpy as np
#array1 = np.array(range(100,200,10))

#print (array1)
#z = range(100,200,10)

#for x, y in np.ndindex((z,2)):
#    print(x, y)

#z = [(x,y) for x in range(100,200,20) for y in range(110,190,20)]

array1 = np.array(range(100,200,10))
array1 = array1.reshape(5, 2)


print (array1)