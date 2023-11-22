#4: Read toothpaste sales data of each month and show it using a scatter plot

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("company_sales_data1.csv")

monthList  = df['month_number'].tolist()
toothpaste = df['toothpaste'].tolist()

plt.plot(monthList, toothpaste, label = 'Tooth paste sales data', ls='', marker = 'o', linewidth = 3)

plt.xlabel('Period in months')
plt.ylabel('Units sold')
plt.grid(linestyle = '--', linewidth = 0.5)

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.yticks([4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000])

plt.legend(loc='upper left')
plt.title('Tooth paste sales data')

plt.show()