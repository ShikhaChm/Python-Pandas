#    The total number of months included in the dataset
#    The total amount of revenue gained over the entire period
#    The average change in revenue between months over the entire period
#    The greatest increase in revenue (date and amount) over the entire period
#    The greatest decrease in revenue (date and amount) over the entire period
import csv
import pandas as pd
import numpy as np

df = pd.read_csv('raw_data/budgetDataOne.csv', delimiter=',', encoding="utf-8-sig")

df.dtypes

df['month'] = [i.split('-')[0] for i in df['Date']]
df.head()
np.unique(df['month'])

len(np.unique(df['Date']))

sum(df['Revenue']

df['ChangeInRev'] = df['Revenue'] - df['PrevMonthRev']

df['PrevMonth'] = df['Date'].shift(1)
df['PrevMonthRev'] = df['Revenue'].shift(1)

np.mean(df['ChangeInRev'])

df.sort_values(by='ChangeInRev').head()
#max revenue change
df.iloc[[1],[0,5]]

#min revenue change
df.iloc[[-1],[0,5]]

