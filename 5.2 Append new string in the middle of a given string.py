#2: Append new string in the middle of a given string
#Given two strings, s1 and s2. Write a program
#to create a new string s3 by appending s2 in the middle of s1.

s1 = "Ault"
s2 = "Kelly"
s3 = ""

s3 = s3 + s1[0]
s3 = s3 + s1[1]
s3 = s3 + s2
s3 = s3 + s1[2]
s3 = s3 + s1[3]

print (s3)