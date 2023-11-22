#4: Write a program to print multiplication table of a given number
#For example, num = 2 so the output should be

userinput = input("Provide your number for multiplication:")
number = int(userinput)

for i in range (1, 11):
	print (number * i)
