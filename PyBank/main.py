#    The total number of months included in the dataset
#    The total amount of revenue gained over the entire period
#    The average change in revenue between months over the entire period
#    The greatest increase in revenue (date and amount) over the entire period
#    The greatest decrease in revenue (date and amount) over the entire period
import csv
import pandas as pd
import numpy as np

print "##################################", "\n"
print "   Analysis of PyBank Dataset","\n", "##################################", "\n"
#df = pd.read_csv('budgetDataOne.csv', delimiter=',', encoding="utf-8-sig")
df = pd.read_csv('budgetDataTwo.csv', delimiter=',', encoding="utf-8-sig")
df.dtypes

print "First few lines of dataset : ", "\n","================================","\n", df.head(),"\n"

df['month'] = [i.split('-')[0] for i in df['Date']]
#f = open("outputFile.txt","w+") 
months = np.unique(df['month'])
#print("The total number of months included in the dataset: ", months)
#    The total number of months included in the dataset
len(np.unique(df['Date']))
print "The total number of months included in the dataset: ", len(np.unique(df['Date'])) ,"\n"

revenue = sum(df['Revenue'])
print "Total amount of revenue gained over the entire period: ", revenue ,"\n"

df['PrevMonth'] = df['Date'].shift(1)
df['PrevMonthRev'] = df['Revenue'].shift(1)
df.loc[pd.isnull(df['PrevMonthRev']),'PrevMonthRev'] = 0
df['ChangeInRev'] = df['Revenue'] - df['PrevMonthRev']
avgChangeInRev = np.mean(df['ChangeInRev'])
print   "The average change in revenue between months over the entire period: ", avgChangeInRev , "\n"

df.sort_values(by='ChangeInRev').head()

#max revenue change
greatestIncRev = df.iloc[[1],[0,5]]
print   "The greatest increase in revenue (date and amount) over the entire period: ","\n",greatestIncRev, "\n"

#    The greatest decrease in revenue (date and amount) over the entire period
#min revenue change,
greatestDecRev = df.iloc[[-1],[0,5]]
print   "The greatest decrease in revenue (date and amount) over the entire period: ","\n",greatestDecRev, "\n"

#f.close()
