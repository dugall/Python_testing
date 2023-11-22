#7: Read the total profit of each month and show it using
#the histogram to see the most common profit ranges

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("company_sales_data1.csv")
profitList = df['total_profit'].tolist()
monthList  = df['month_number'].tolist()

plt.bar(monthList, profitList)

plt.xlabel('Period in months')
plt.ylabel('Profit in USD')

plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])

plt.title('Company profit per month')

plt.show()