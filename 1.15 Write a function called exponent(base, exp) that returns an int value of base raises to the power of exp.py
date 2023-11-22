#15: Write a function called exponent(base, exp)
#that returns an int value of base raises to the power of exp

import math
def exponent(base, exp):
	z = math.pow(base, exp)
	return z

print (exponent(4, 5))