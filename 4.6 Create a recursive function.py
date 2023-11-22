#6: Create a recursive function
#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
#A recursive function is a function that calls itself again and again.

n = 10

def summary (n):
    if n == 0:
        return n
    return n + summary(n - 1)

print (summary(n))

#https://stackoverflow.com/questions/19966290/recursive-function-to-calculate-sum-of-1-to-n