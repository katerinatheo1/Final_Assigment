#Import essential libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Create dataframe from csv file
df = pd.read_csv('finance_liquor_sales.csv')

#Run basic analysis and review of dataframe
summary = df.describe()
print(summary)

#Create dataframe with essential columns and aggregation per bottles sold and sale dollars
q = df.groupby(['zip_code','store_number','item_description'],as_index=False).agg({'bottles_sold':'sum','sale_dollars':'sum'})

#Print new dataframe and export it into csv file for further analysis
print(q)
q.to_csv(r'/Users/katerinatheofanopoulou/PycharmProjects/pythonProject1/finance_liquor.csv', index=False)




