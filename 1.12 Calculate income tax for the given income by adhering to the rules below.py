#Calculate income tax for the given income by adhering to the rules below
#Taxable Income	Rate (in %)
#First $10,000	0
#Next $10,000	10
#The remaining	20
#For example, suppose the taxable income is 45000, and the income tax payable is
#10000*0% + 10000*10%  + 25000*20% = $6000.

def taxes(income):
	
	
#	if income <= 10000: taxes2pay = 0
#	elif income > 10000: taxes2pay = taxes2pay_10000 = (income - 10000) * 0.1
#	elif income > 20000: taxes2pay = (income - 20000) * 0.2 + taxes2pay_10000

	if ((income >= 10000) and (income <= 20000)): taxe2pay = round((income - 10000) * 0.1, 2)
	elif income > 20000: taxe2pay = round(((20000 - 10000) * 0.1 + (income - 20000) * 0.2), 2)

	return taxe2pay

print ("You have tp pay $", taxes(50000))

#10000*0+10000*0.1+30000*0.2 = 7000