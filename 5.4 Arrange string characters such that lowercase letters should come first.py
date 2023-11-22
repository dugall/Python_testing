#4: Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters.
#Write a program to arrange the characters of a string so that all
#lowercase letters should come first.

str1 = "PyNaTive"
str2 = ""

for i in str1:
	if i == i.lower(): str2 = str2 + i

for i in str1:
	if i == i.upper(): str2 = str2 + i

print(str2)


