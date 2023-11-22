#Write a program to remove characters from a string starting from zero up to n and
#return a new string.
#
#For example:
#
#remove_chars("pynative", 4) so output must be tive. Here, we need to remove
#the first four characters from a string.
#remove_chars("pynative", 2) so output must be native. Here, we need to remove
#the first two characters from a string.
#Note: n must be less than the length of the string.

string = "pynative"
n = 4
if n < len(string): print (string[n:])
n = 2
if n < len(string): print (string[n:])
