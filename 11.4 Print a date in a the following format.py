#4: Print a date in a the following format
#Day_name  Day_number  Month_name  Year

from datetime import datetime

given_date = datetime(2020, 2, 25)

print (given_date.strftime("%A %w %B %Y"))

#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

