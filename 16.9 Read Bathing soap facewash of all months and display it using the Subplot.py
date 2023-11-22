#9: Read Bathing soap and facewash of all months and display it using the Subplot

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("company_sales_data1.csv")

monthList  = df['month_number'].tolist()
bathingsoap = df['bathingsoap'].tolist()
facewash = df['facewash'].tolist()

plt.subplot(2, 1, 2)
plt.plot(monthList, bathingsoap, color = 'k', marker = 'o', linewidth = 3)

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.yticks([7500, 10000, 12500])

plt.title('Sales data of Bathingsoap')

###

plt.subplot(2, 1, 1)
plt.plot(monthList, facewash, color = 'r', marker = 'o', linewidth = 3)

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.yticks([1500, 2000])

plt.title('Sales data of Facewash')

plt.show()