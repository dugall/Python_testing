#8: Generate random secure token of 64 bytes and random URL

import random
import secrets

new_token = secrets.token_bytes(64)

password_reset = "https://www2.hm.com/en_ca/profile/reset="
password_reset += secrets.token_urlsafe(99)

print (new_token, "\n\n", password_reset)


