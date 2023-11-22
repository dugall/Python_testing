#4: Initialize dictionary with default values
#In Python, we can initialize the keys with the same values.
#{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_dic = dict.fromkeys(employees, defaults)

print (new_dic)

#https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/