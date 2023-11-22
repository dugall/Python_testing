#18: Replace each special symbol with # in the following string

import re

str1 = '/*Jon is @developer & musician!!'

#str2 = re.sub("!@$%^&*()[]{};:,./<>?`~-=_+", "#", str1)
#print(str2)


str2 = ''.join("#" if c in '!~@$%^&*()-+={}[]:;<.>?/\'' else c for c in str1)

print(str2)

#https://stackoverflow.com/questions/47295108/special-characters-replace-using-regex-in-python

#removeSpecialChars = str1.replace("!@$%^&*()[]{};:,./<>?`~-=_+", "#")


#str2 = "".join(i for i in str1 if i.isalnum())


#str2 = str1.replace(string.punctuation, "#")

#for i in str1:
#	if i in string.punctuation: 
		

		#i = "#"

#print (removeSpecialChars)