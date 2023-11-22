#9: Calculate the date 4 months from the current date
from datetime import datetime
from dateutil.relativedelta import relativedelta


given_date = datetime(2020, 2, 25).date()

new_date = given_date + relativedelta(months=+4)

print(new_date)

#https://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime