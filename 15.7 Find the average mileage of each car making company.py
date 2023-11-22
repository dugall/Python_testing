#7: Find the average mileage of each car making company

import pandas as pd

df = pd.read_csv('Automobile_data1.csv')

Sort_company = df.groupby('company')

Sort_max = Sort_company['average-mileage'].mean()

print (Sort_max)
