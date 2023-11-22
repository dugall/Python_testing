#6: Add a week (7 days) and 12 hours to a given date
import datetime

given_date = datetime.datetime(2020, 3, 22, 10, 0, 0)

time_change = datetime.timedelta(days=7, hours=12) 

new_time = given_date + time_change

print (new_time)