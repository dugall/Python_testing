#4: Count the occurrence of each element from a list
#Write a program to iterate a given list and count
#the occurrence of each element and create a dictionary to show the count of each element.

from collections import Counter

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

print (Counter(sample_list))

####

counter_dic = dict()

for i in sample_list:
	if i in counter_dic: counter_dic[i] +=1
	else: counter_dic[i] =1

print (counter_dic)