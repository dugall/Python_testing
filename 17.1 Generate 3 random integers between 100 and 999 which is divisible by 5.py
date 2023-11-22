#1: Generate 3 random integers between 100 and 999 which is divisible by 5

import random

z = range (3)

for x in z:
	print (random.randrange(100, 999, 5))
