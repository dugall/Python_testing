#10: Write a program to count occurrences of all characters within a string

from collections import Counter

str1 = "Apple"
str1 = str1.lower()
c = Counter(str1)
#symbols = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()! "
#count1 = 0

for i, ct in c.items():
#    if i not in seen and i in symbols:
#       count1 = str1.count(i)
    print (i, "occured", ct, "times")

#https://stackoverflow.com/questions/29225682/count-the-occurrence-of-characters-in-a-string