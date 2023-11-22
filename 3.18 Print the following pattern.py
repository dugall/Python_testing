#18: Print the following pattern
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#*

lines = 5

for i in range (0, lines):
	for j in range (1, i+1):
		print ("* ", end = "")
	print ("* ")
for i in range (lines, 1, -1):
	for j in range (1, i-1):
		print ("* ", end = "")
	print ("* ")