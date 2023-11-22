#The Fibonacci Sequence is a series of numbers.
#The next number is found by adding up the two numbers before it.
#The first two numbers are 0 and 1.

#For example, 0, 1, 1, 2, 3, 5, 8, 13, 21.
#The next number in this series above is 13+21 = 34.

x = 0
y = 1

for i in range (0, 10):
	print (x)
	result = x + y
	x = y
	y = result


	