#7: Convert the following JSON into Vehicle Object
from __future__ import print_function
import json

try:
    from types import SimpleNamespace as sn
#https://stackoverflow.com/questions/28496958/creating-a-short-alias-for-imported-variable-import-types-simplenamespace-as-n
#SimpleNamespace is not defined
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

data = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'

# Parse JSON into an object with attributes corresponding to dict keys.
y = json.loads(data, object_hook=lambda d: sn(**d))
print(y.name, y.engine, y.price)

#https://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object

#def vehicleDecoder(obj):
#        return Vehicle(obj['name'], obj['engine'], obj['price'])

#vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
#           object_hook=vehicleDecoder)