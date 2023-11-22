#17: Find words with both alphabets and numbers
#Write a program to find words with both alphabets and numbers from an input string.

str1 = "Emma25 is Data scientist50 and AI Expert"
result = []
str2 = str1.split()

for i in str2:
	if any(character.isalpha() for character in i) and any(character.isdigit() for character in i): 
   		result.append(i) 

print (result)

