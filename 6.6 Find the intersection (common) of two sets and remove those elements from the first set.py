#6: Find the intersection (common) of two sets and remove those elements from the first set

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

temp_set = [i for i in first_set if i in second_set]

print (temp_set)

for i in temp_set:
	first_set.remove(i)

print (first_set)