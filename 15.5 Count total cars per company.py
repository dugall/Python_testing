#5: Count total cars per company

#4: Print All Toyota Cars details

import pandas as pd

df = pd.read_csv("Automobile_data.csv")

z = df['company'].value_counts()

print (z)
