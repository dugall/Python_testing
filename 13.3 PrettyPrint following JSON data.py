#3: PrettyPrint following JSON data

import json
import pprint

sampleJson = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}

pp = json.dumps(sampleJson, indent=2, separators=(",", " = "))

print(pp)

#https://pynative.com/python-prettyprint-json-data/