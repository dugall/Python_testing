#10: Generate a random date between given start and end dates

import random
import time

def RandomDateGenerator(startDate, endDate):
	randomGenerator = random.random()
	format_date = '%d-%m-%Y'

	startTime = time.mktime(time.strptime(startDate, format_date))
	endTime = time.mktime(time.strptime(endDate, format_date))

	randomTime = startTime + randomGenerator * (endTime - startTime)
	randomDate = time.strftime(format_date, time.localtime(randomTime))
    
	return randomDate

print (RandomDateGenerator("15-11-2019", "12-08-2023"))