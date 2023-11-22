#7: Print the following pattern

row = 5
column = 5

for i in range (0, row + 1):
	for j in range (column - i, 0, -1):
		print (j, end=" ")
	print ()		

#print (j, end=" ")

#line = 5 
#
#for i in range(1, line + 1, 1):
#	for j in range (1, i + 1):
#		print (j, end=" ")
#	print ()
