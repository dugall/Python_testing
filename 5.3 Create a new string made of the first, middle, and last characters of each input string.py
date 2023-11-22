#3: Create a new string made of the first, middle, and last characters of each input string
#Given two strings, s1 and s2, write a program to return
#a new string made of s1 and s2’s first, middle, and last characters.

s1 = "America"
s2 = "Japan"

FirstLetter = s1[0] + s2[0]
MiddleLetter = s1[int(len(s1)/2)] + s2[int(len(s1)/2)-1]
LastLetter = s1[int(len(s1)-1)] + s2[int(len(s2)-1)]

Final = FirstLetter + MiddleLetter + LastLetter

print(Final)


