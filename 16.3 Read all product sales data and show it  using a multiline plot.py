#3: Read all product sales data and show it  using a multiline plot

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

plt.plot(monthList, facecream, label = 'Facecream', color = 'r', marker = 'o', linewidth = 3)
plt.plot(monthList, facewash, label = 'Facewash', color = 'b', marker = 'o', linewidth = 3)
plt.plot(monthList, toothpaste, label = 'Toothpaste', color = 'y', marker = 'o', linewidth = 3)
plt.plot(monthList, bathingsoap, label = 'Bathingsoap', color = 'g', marker = 'o', linewidth = 3)
plt.plot(monthList, shampoo, label = 'Shampoo', color = 'c', marker = 'o', linewidth = 3)
plt.plot(monthList, moisturizer, label = 'Moisturizer', color = 'm', marker = 'o', linewidth = 3)

plt.xlabel('Period in months')
plt.ylabel('Units sold')

plt.legend(loc='upper left') #pick a text from 'label'

plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])

plt.title('Company sales data of the last year')

plt.show()