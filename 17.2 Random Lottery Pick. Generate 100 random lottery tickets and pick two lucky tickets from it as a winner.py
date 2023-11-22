#2: Random Lottery Pick. Generate 100 random lottery tickets
#and pick two lucky tickets from it as a winner.
#All 100 ticket number must be unique.

import random

#randomlist = random.sample(range(1000), 10)
#print(randomlist)
#randomlist = random.sample(range(1000), 10)
#print(randomlist)

randomlist = []

for i in range (1, 100):
	randomlist.append(random.randrange(10000, 99999))

print (random.sample(randomlist, 2))

