#5: Create a dictionary by extracting the keys from a given dictionary
#Write a Python program to create a new dictionary by extracting
#the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

for i in keys:
	print (i, sample_dict.get(i))

#https://stackoverflow.com/questions/24204087/how-to-get-multiple-dictionary-values