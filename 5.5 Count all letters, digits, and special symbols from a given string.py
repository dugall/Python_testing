#5: Count all letters, digits, and special symbols from a given string
#Total counts of chars, digits, and symbols 
#Chars = 8 
#Digits = 3 
#Symbol = 4

str1 = "P@#yn26at^&i5ve"
chars = 0
digits = 3
symbols = 4

special_characters = "!@#$%^&*()-+?_=,<>/"
numbers = "123456789"

for i in str1:
	if i == special_characters: symbols += 1
	elif i == numbers: digits +=1
	else: chars += 1

print ("Total counts of chars, digits, and symbols:\n",
		"\nSymbols = ", symbols, "\nDigits = ", digits, "\nChars = ", chars)