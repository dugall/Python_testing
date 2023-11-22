#4: Print All Toyota Cars details

import pandas as pd

df = pd.read_csv("Automobile_data.csv")

z = pd.DataFrame(df)

Sort_company = z.groupby('company')

Sort_toyota = Sort_company.get_group("toyota")

print(Sort_toyota)