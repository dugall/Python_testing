#10: Read all product sales data and show it using the stack plot

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("company_sales_data1.csv")

monthList  = df['month_number'].tolist()
facecream = df['facecream'].tolist()
facewash = df['facewash'].tolist()
toothpaste = df['toothpaste'].tolist()
bathingsoap = df['bathingsoap'].tolist()
shampoo = df['shampoo'].tolist()
moisturizer = df['moisturizer'].tolist()

plt.stackplot(monthList, facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer)

plt.xlabel('Period in months')
plt.ylabel('Units sold')

plt.legend(loc='upper left') #pick a text from 'label'

plt.xticks(monthList)
plt.yticks([5000, 10000, 15000, 20000, 25000, 30000])

plt.title('All product sale data')

plt.show()