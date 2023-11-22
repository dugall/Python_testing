#3: Return multiple values from a function
#Write a program to create function calculation() such that it can
#accept two variables and calculate addition and subtraction.
#Also, it must return both addition and subtraction in a single return call.

def calculation(a, b):
    
    x = a + b
    y = a - b
    return x, y
    
res = calculation(40, 10)
print(res)