#7: String characters balance Test
#Write a program to check if two strings are balanced. For example
#strings s1 and s2 are balanced if #all the characters in the s1 are present in s2.
#The character’s position doesn’t matter.

#s1 = "Yn"
#s2 = "PYnative"
#leng1 = str(len(s1))

#for i in s1:
#print (s1 in s2)

#print (s1 in s2)

def stringtest (s1, s2):
	marker = True
	for i in s1:
		if i in s2: continue
		else: 
			marker = False
	return marker


s1 = "Ynf"
s2 = "PYnative"

stringtest (s1, s2)

#s1 = "Yn"
#s2 = "PYnative"

marker = stringtest (s1, s2)

print (marker)