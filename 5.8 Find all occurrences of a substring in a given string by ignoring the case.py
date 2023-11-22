#8: Find all occurrences of a substring in a given string by ignoring the case
#Write a program to find all occurrences of “USA” in a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it?"
seekstring = "USA"

string2 = str1.lower()
counting = string2.count(seekstring.lower())

print (counting)