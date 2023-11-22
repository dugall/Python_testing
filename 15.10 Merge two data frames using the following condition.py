#10: Merge two data frames using the following condition
import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

z = pd.DataFrame(Car_Price)
y = pd.DataFrame(car_Horsepower)

f = z.merge(y, on='Company')

print (f)


#https://stackoverflow.com/questions/45420474/pandas-merge-adding-column