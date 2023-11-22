#8: Calculate total sale data for last year for each product and show it using a Pie chart

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("company_sales_data1.csv")

facecream = df['facecream'].sum()
facewash = df['facewash'].sum()
toothpaste = df['toothpaste'].sum()
bathingsoap = df['bathingsoap'].sum()
shampoo = df['shampoo'].sum()
moisturizer = df['moisturizer'].sum()

colors = ["gold", "darkviolet", "blue", "orange", "green", "red"]
labels = ["Facecream", "Facewash", "Toothpaste", "Bathingsoap", "Shampoo", "Moisturizer"]

plt.pie([facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer],
	labels = labels, autopct='%1.1f%%', colors = colors)

plt.legend(loc='lower right')
plt.title('Company sales data of the last year')

plt.show()