#Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse.
#For example, 545, is the palindrome numbers

#def palindrome(number):
#
#	string = int(number)
#	if(string == string[::-1]): print("The string is a palindrome")
#	else: print("Not a palindrome")
#
#print (palindrome(123123))

import math
def rev(num):
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          rev(num // 10))
 
# initializing number 
test_number = 123123123123
 
# printing the original number 
print ("The original number is : " + str(test_number))
 
# using math.log() + recursion + list comprehension
# for checking a number is palindrome
res = test_number == rev(test_number)
 
# printing result
print ("Is the number palindrome ? : " + str(res))

#https://www.geeksforgeeks.org/python-program-to-check-if-number-is-palindrome-one-liner/