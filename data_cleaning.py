import pandas as pd
import numpy as np

df=pd.read_csv("out.csv")
#, delimiter=',', encoding="utf-8-sig"

#Removing rows with cells having value '0'
df = df[df.billed_units!= 0]

#df.to_csv('out.csv')

#group = df.groupby('consumer_num')['billed_units'].unique()
#
# group[group.apply(lambda x: len(x)>1)]
#
# df = group.to_frame()

#bill_units=df['billed_units'].tolist()

c = 'consumer_num'

m = 'month {}'.format

df=df.set_index(
    [c, df.groupby(c).cumcount() + 1]
).billed_units.unstack().rename(columns=m).iloc[:, :6].reset_index()

d1 = df.dropna()

print d1

d1.to_csv("final.csv")

#print df.head(10)

