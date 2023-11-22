#6: Read sales data of bathing soap of all months and show it using a bar chart.
#Save this plot to your hard disk

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("company_sales_data1.csv")

monthList  = df['month_number'].tolist()
bathingsoap = df['bathingsoap'].tolist()

r1 = range(1, 13) #numbers of bars
width1 = 0.7 #width between bars stacks

plt.bar(r1, bathingsoap, label = 'Facecream sales data', width=width1)

plt.xlabel('Period in months')
plt.ylabel('Units sold')
plt.grid(linestyle = '--', linewidth = 0.5)

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.yticks([2000, 4000, 6000, 8000, 10000, 12000, 14000])

plt.legend(loc='upper left')
plt.title('Facecream sales data')

plt.savefig("sales_data.png", dpi=300)

plt.show()