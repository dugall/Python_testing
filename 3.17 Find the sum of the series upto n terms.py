#17: Find the sum of the series upto n terms
#Write a program to calculate the sum of series up to n term.
#For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690


def calculation(n):
	number = 3
	z = 0

	for i in range (1, n+1):
		z = z + number
		number = (number * 10) + 3

	return z
         
n = 5
#3 + 33 + 333 + 3333 + 33333
print(calculation(n))
