#5: Generate random String of length 5

import random
import string

chars = string.ascii_uppercase + string.ascii_lowercase
string_range = range(5)

final_string = "".join(random.choice(chars) for i in range(5))

print (final_string)

