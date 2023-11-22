#Write a function to return True if the first and last number of a given list is same.
#If numbers are different then return False.



#if numbers_x[0] == numbers_x[-1]: print (True)

def number_check(ReceivedList):

	first_letter = ReceivedList[0]
	last_letter = ReceivedList[-1]

	if first_letter == last_letter: return (True)
	else: return (False)

numbers_x = [10, 20, 30, 40, 10]
print (number_check(numbers_x))
numbers_y = [75, 65, 35, 75, 30]
print (number_check(numbers_y))