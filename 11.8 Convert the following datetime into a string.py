#8: Convert the following datetime into a string
import datetime

given_date = datetime.datetime(2020, 2, 25)

new_time = given_date.strftime("%Y-%m-%d %H:%M:%S")

print (new_time)
