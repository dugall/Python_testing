#6: Generate a random Password which meets the following conditions
#Password length must be 10 characters long.
#It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

import random
import string
import secrets

characters = string.ascii_letters + string.ascii_uppercase + string.digits + string.punctuation
new_pass = random.sample(characters, 6)
new_pass += random.sample(string.ascii_uppercase, 2)
new_pass += random.sample(string.digits, 1)
new_pass += random.sample(string.punctuation, 1)

#new_pass = ''.join(random.choice(characters) for i in range(10))

make_it_list = list(new_pass)
secrets.SystemRandom(make_it_list)
random.shuffle(make_it_list)
shuffled = "".join(make_it_list)

print (shuffled)