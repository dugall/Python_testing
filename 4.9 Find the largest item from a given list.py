#9: Find the largest item from a given list

x = [4, 6, 8, 24, 12, 2]
maxnumber = 0

for i in x:
	if maxnumber < i: maxnumber = i

print (maxnumber)

####

print (max(x))