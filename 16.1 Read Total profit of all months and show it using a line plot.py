#1: Read Total profit of all months and show it using a line plot
#Total profit data provided for each month. Generated line plot must include the following properties: –
#X label name = Month Number
#Y label name = Total profit


import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

plt.rcParams["figure.figsize"]
plt.rcParams["figure.autolayout"] = True
columns = ["month_number", "total_profit"]

msft = pd.read_csv('company_sales_data1.csv')

plt.plot(msft.month_number, msft.total_profit)
plt.show()


#https://matplotlib.org/3.2.2/gallery/misc/plotfile_demo_sgskip.html
#https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib


df = pd.read_csv("company_sales_data1.csv")
profitList = df['total_profit'].tolist()
monthList  = df['month_number'].tolist()

plt.plot(monthList, profitList)

plt.xlabel('Period in months')
plt.ylabel('Profit in USD')

plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])

plt.title('Company profit per month')

plt.show()