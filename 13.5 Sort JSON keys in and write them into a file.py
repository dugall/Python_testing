#5: Access the nested key ‘salary’ from the following JSON

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

j = json.loads(sampleJson)

print (j["company"]["employee"]["payble"]["salary"])