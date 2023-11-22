#Write a Program to extract each digit from an integer in the reverse order.

#For example, If the given int is 7536,
#the output shall be “6 3 5 7“, with a space separating the digits.

def reverseInteger(number):
#number = [123123]
	
	number = int(number)
	theresult = []

	while number > 0:
   		rem = number % 10
   		number = int(number / 10)
   		theresult.append(rem)

	return theresult

print (reverseInteger(512312313))

#https://www.geeksforgeeks.org/python-split-a-list-having-single-integer/
