#4: Sort JSON keys in and write them into a file

import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

x = json.dumps(sampleJson, sort_keys=True)

print (x)
