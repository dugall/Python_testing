#9: Roll dice in such a way that every time you get the same number
#Dice has 6 numbers (from 1 to 6). Roll dice in such a way
#that every time you must get the same output number. do this 5 times.

import random

numbers = [1,2,3,4,5,6]

for i in range(5):
    random.seed(30)
    print(random.choice(numbers))


