#3: Generate 6 digit random secure OTP

import random
import secrets

SecretsGen = secrets.SystemRandom()
number = SecretsGen.randint(100000, 999999)

print (number)