#Remove and add item in a list
#Write a program to remove the item present at index 4 and add
#it to the 2nd position and at the end of the list.
#List After removing element at index 4  [34, 54, 67, 89, 43, 94]
#List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
#List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]

list1 = [34, 54, 67, 89, 11, 43, 94]
list2 = list1[4]

del list1[4]

list1.insert(2, list2)

list1.append(list2)

print (list1)


#https://stackoverflow.com/questions/3748063/what-is-the-syntax-to-insert-one-list-into-another-list-in-python