#Write a program to check if the given file is empty or not

#import os
#os.stat("text.txt").st_size == 0

#file1 = open("text.txt", "r")
#
#x = []
#
#for x in file1:
#	if x == "":
#		print ("This file is empty")

from pathlib import Path

thepatch = Path("text.txt")

print (True) if thepatch.stat().st_size == 0 else print(False)

#https://stackoverflow.com/questions/2507808/how-to-check-whether-a-file-is-empty-or-not