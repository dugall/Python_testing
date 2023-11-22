#Write a program to 
#Create a new list that contains the 0th index item from both the list,
#then the 1st index item, and so on till the last element.
#any leftover items will get added at the end of the new list.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = []

#for i in list1:
#	for j in list2:
#		new_list = i + j

#new_list = [x+y for x in list1 for y in list2]


#new_list = [list(x) for x in zip(list1, list2)]


#for m, n in zip(list1, list2):
#	m + n

for i, j in zip(list1, list2):
    new_list.append(f'{i}{j}')
#    new_list.append(f'{j}{i}')

print (new_list)



#https://stackoverflow.com/questions/70730533/how-to-concatenate-strings-from-two-different-list-index-wise-in-commutative-way
#https://stackoverflow.com/questions/26434925/in-python-how-do-i-merge-lists-element-wise
#https://stackoverflow.com/questions/43386075/concatenating-two-lists-of-strings-element-wise-in-python-without-nested-for-loo
#https://stackoverflow.com/questions/19560044/how-to-concatenate-element-wise-two-lists-in-python
