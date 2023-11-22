#4: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = [x+y for x in list1 for y in list2]

print (list3)

#https://stackoverflow.com/questions/43386075/concatenating-two-lists-of-strings-element-wise-in-python-without-nested-for-loo
