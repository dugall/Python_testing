#5: Read face cream and facewash product sales data and show it using the bar chart

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("company_sales_data1.csv")

monthList  = df['month_number'].tolist()
facecream = df['facecream'].tolist()
facewash = df['facewash'].tolist()

r1 = np.arange(12) #numbers of bars
width1 = 0.25 #width between bars stacks
 
# Create the first subplot
plt.bar(r1+0.16, facecream, label = 'Facecream sales data', width=width1)
plt.bar(r1-0.16, facewash, label = 'Facewash sales data', width=width1)
#plt.grid(True, linewidth= 1, linestyle="--")


#plt.plot(monthList, facecream, label = 'Facecream sales data', color = 'r', marker = 'o', linewidth = 3)
#plt.plot(monthList, facewash, label = 'Facewash sales data', color = 'b', marker = 'o', linewidth = 3)
#plt.bar(facecream, color ='r', height = facecream, width = barWidth, edgecolor ='green', label ='facecream') 
#plt.bar(facewash, color ='g', height = facewash, width = barWidth, edgecolor ='red', label ='facewash') 
#plt.bar(br3, CSE, color ='b', width = barWidth, 
#        edgecolor ='grey', label ='CSE') 

#plt.bar(facecream, facewash)

plt.xlabel('Period in months')
plt.ylabel('Units sold')
plt.grid(linestyle = '--', linewidth = 0.5)

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
#plt.yticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500])

plt.legend(loc='upper left')
plt.title('Facewash and Facecream sales data')

plt.show()