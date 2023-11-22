#1B: Create a string made of the middle three characters

str1 = "JhonDipPeta"
string2 = ""

middle = int(len(str1)/2)

string2 = string2 + str1[middle-1]
string2 = string2 + str1[middle]
string2 = string2 + str1[middle+1]

print (string2)