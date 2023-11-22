#10: Remove duplicates from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique = []

minimum = min(sample_list)
maximum = max(sample_list)

for i in sample_list:
	if i not in unique: unique.append(i)

newtuple = ()
newtuple = unique

print (minimum, maximum)
print (newtuple)
