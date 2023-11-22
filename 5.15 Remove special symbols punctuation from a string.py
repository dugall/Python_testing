#15: Remove special symbols / punctuation from a string

import string 

str1 = "/*Jon is @developer & musician"
str2 = ""

for i in str1:
	if i not in string.punctuation:
		str2 += i

print (str2)

#https://stackoverflow.com/questions/31774548/getting-error-while-using-string-punctuation-python