#2: Get total profit of all months and show line plot with the following Style properties

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("company_sales_data1.csv")

profitList = df['total_profit'].tolist()
monthList  = df['month_number'].tolist()

plt.plot(monthList, profitList, label = 'Profit data of the last year',
	color = 'r',
	marker = 'o',
	markerfacecolor = 'k',
	linestyle = '--',
	linewidth = 3)

plt.xlabel('Period in months')
plt.ylabel('Profit in USD')

plt.legend(loc='lower right') #pick a text from 'label'

plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])

plt.title('Company sales data of the last year')

plt.show()