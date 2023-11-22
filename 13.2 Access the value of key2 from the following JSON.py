#2: Access the value of key2 from the following JSON

import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

x = json.loads(sampleJson)

print(x["key2"])