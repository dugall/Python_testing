#9: Parse the following JSON to get all the values of a key ‘name’ within an array
from __future__ import print_function
import json

data = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

resp = []

resp = json.loads(data)

#dataList = [item.get('name') for item in resp]
#print(dataList)

for i in resp:
    for attribute, value in i.items():
    	if attribute == "name":
        	print(value)

#https://stackoverflow.com/questions/2733813/iterating-through-a-json-object

#for i in resp:
#	if i == "name":
#		x = i.get("name")
#		print (x)


#if "name" in resp:
#	print(resp["name"])



#for k, v in resp.items():
#	print (k)

#print (resp)

#value = resp.get("name")

#for value in resp:
#	if i == 'name':
#		print (i)

