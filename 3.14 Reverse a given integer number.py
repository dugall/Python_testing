#14: Reverse a given integer number
#Given:
#
#76542
# Expected output:
#24567

num = 76542
print(str(num)[::-1])

num = 76542
rev_number = 0

while num != 0:
	digit = num % 10
	rev_number = rev_number * 10 + digit
	num = num // 10

print (rev_number)
