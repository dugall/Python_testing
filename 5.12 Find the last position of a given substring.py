#12: Find the last position of a given substring
#Write a program to find the last position of a substring “Emma” in a given string.

str1 = "Emma is a data scientist who knows Python. Emma works at google."
str2 = "Emma"
index = 0

for str2 in str1:
	if str2 in str1: index = str1.index("Emma")

print (index)

###

index = str1.rfind("Emma")
print (index)