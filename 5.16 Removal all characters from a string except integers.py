#16: Removal all characters from a string except integers

str1 = 'I am 25 years and 10 months old'

newstring = int(''.join(filter(str.isdigit, str1)))

print (newstring)

#https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
