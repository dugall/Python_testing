#9: Concatenate two data frames using the following conditions

import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

z = pd.DataFrame(GermanCars)
y = pd.DataFrame(japaneseCars)

df_row = pd.concat([z, y])

#df_row = pd.merge(z, y, on='Company', how='outer')
#z.join(y, lsuffix='_left', rsuffix='_right')


print(df_row)

#https://www.datacamp.com/tutorial/joining-dataframes-pandas?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720821&utm_adgroupid=157156375191&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=680291483655&utm_targetid=aud-438999696719:dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9000970&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-row-p1_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-bfcm23&gad_source=1&gclid=CjwKCAiAu9yqBhBmEiwAHTx5p5dm8ZoBuNY-pK9enlGERMBzdi-i_wdM29uYjRv_m1PQUGgKzdR-rRoCxDEQAvD_BwE
#https://pandas.pydata.org/docs/reference/api/pandas.concat.html

