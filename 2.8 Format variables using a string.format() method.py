#Exercise 8: Format variables using a string.format() method.
#Write a program to use string.format() method to format the following three variables
#as per #the expected output
#
#Given:
#
#totalMoney = 1000
#quantity = 3
#price = 450

string = "I have {totalMoney:} dollars so I can buy {quantity:} football for {price:.2f} dollars."

print (string.format(totalMoney = 1000, quantity = 3, price = 450))