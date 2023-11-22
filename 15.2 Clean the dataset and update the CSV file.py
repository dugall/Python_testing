#2: Clean the dataset and update the CSV file
#Replace all column values which contain ?, n.a, or NaN.

import pandas as pd

df = pd.read_csv('Automobile_data1.csv', na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})

df.to_csv('Automobile_data1.csv')