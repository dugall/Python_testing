#5: Create a Python set such that it shows the element from both lists in a pair
#Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}


first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
#mylist = []
#myset = {}

for i in first_list:
	for j in second_list:
		if i*i == j: x = zip(first_list, second_list)
#			mylist = mylist.append(i, j)
#			myset.update(mylist)

print (set(x))