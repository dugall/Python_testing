#5: Accept a list of 5 float numbers as an input from the user

input_numbers = []

for i in range (1, 6):
	print ("Print a floating number", i)
	received = float(input())

	input_numbers.append(received)

print (input_numbers)