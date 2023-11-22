#6: Write all content of a given file into a new file by skipping line number 5
#Create a test.txt file and add the below content to it.

file1 = open("text.txt", "r")
file2 = open("new_file.txt", "w")
count = 0

for line in file1:
	if count != 4: file2.write(line)
	count = count +1


