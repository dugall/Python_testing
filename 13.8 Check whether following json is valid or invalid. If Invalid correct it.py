#8: Check whether following json is valid or invalid. If Invalid correct it
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

x = json.loads(sampleJson)