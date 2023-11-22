#14: Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

#if "" and None in str_list:
#    str_list.remove("''")
#    str_list.remove(None)

#print (str_list)

#str_list = list(filter(None, str_list))
#str_list = str_list.remove('')
#str_list = list(filter((""), str_list))

#print (str_list)

y = [x for x in str_list if x]
print (y)

#https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings