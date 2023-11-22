#Generate a Python list of all the even numbers between 4 to 30

for i in range (4, 30):
	if i % 2 == 0:
		print (i)


print(list(range(4,30,2)))