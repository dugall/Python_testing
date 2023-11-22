#6: Find each company’s Higesht price car

import pandas as pd

df = pd.read_csv('Automobile_data1.csv')

Sort_company = df.groupby('company')

Sort_max = Sort_company['price'].max()

print (Sort_max)

