#Print the sum of the current number and the previous number
#Expected Output:
#Printing current and previous number sum in a range(10)
#Current Number 0 Previous Number  0  Sum:  0
#Current Number 1 Previous Number  0  Sum:  1
#Current Number 2 Previous Number  1  Sum:  3
#Current Number 3 Previous Number  2  Sum:  5
#Current Number 4 Previous Number  3  Sum:  7
#Current Number 5 Previous Number  4  Sum:  9
#Current Number 6 Previous Number  5  Sum:  11
#Current Number 7 Previous Number  6  Sum:  13
#Current Number 8 Previous Number  7  Sum:  15
#Current Number 9 Previous Number  8  Sum:  17

x = range (10)
for current_number in x:
    previous_number = 0
    if current_number == 0: previous_number = current_number
    else: previous_number = (current_number - 1)
#    current_number = i
#    if i = 0 previous_number = i - 1
#    if previous_number <= 0: previous_number = current_number
#        return 
    sum_range = current_number + previous_number
    print ("Current Number ", current_number, "Previous Number  ", previous_number,
            "Sum:  ", sum_range)


