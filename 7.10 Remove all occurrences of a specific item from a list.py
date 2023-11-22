#10: Remove all occurrences of a specific item from a list.

list1 = [5, 20, 15, 20, 25, 50, 20]

for i in list1:
	if i == 20 in list1: list1.remove(i)

print (list1)