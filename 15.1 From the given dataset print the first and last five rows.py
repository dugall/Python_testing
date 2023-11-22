#1: From the given dataset print the first and last five rows

import pandas as pd

df = pd.read_csv('Automobile_data.csv')


print(df.loc[0:5]) 

print(df.tail(5)) 

#https://sparkbyexamples.com/pandas/pandas-get-last-row-from-dataframe/