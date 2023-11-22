#10: Read line number 4 from the following file

file1 = open("test.txt", "r")

content = file1.readlines() 
print(content[3])

