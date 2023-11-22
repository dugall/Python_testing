#8: Sort all cars by Price column

import pandas as pd

df = pd.read_csv('Automobile_data1.csv')

sorted_df = df.sort_values(by='price', ascending=False)

print (sorted_df)
