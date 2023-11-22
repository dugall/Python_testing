#9: Replace list’s item with new value if found
#You have given a Python list. Write a program to find value 20 in the list,
#and if it is present, replace it with 200. Only update the first occurrence of an item.

list1 = [5, 10, 15, 20, 25, 50, 20]
list2 = []

for i in list1:
	if i == 20: list2.append(200)
	else: list2.append(i)

print (list2)