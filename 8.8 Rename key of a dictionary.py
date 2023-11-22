#8: Rename key of a dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict["name11"] = sample_dict.pop("name")

print (sample_dict)

####

x = {"name11" if i == "name" else i:v for i,v in sample_dict.items()}

print (x)
