#Create a new list from two list using the following condition
#Given two list of numbers, write a program to create
#a new list such that the new list should contain odd numbers
#from the first list and even numbers from the second list.

#result list: [25, 35, 40, 60, 90]

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

newlist = []

for x in list1:
	if x%2 == 0: newlist.append(x)

for y in list2:
	if y%2 != 0: newlist.append(y)

print (newlist)