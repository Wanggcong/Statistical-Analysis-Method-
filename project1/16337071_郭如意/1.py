
"""
Created on Tue Oct 23 19:26:09 2018

@author: gym
"""

import pandas as pd
import numpy as np

df = pd.read_csv('000001.csv')
#print (df['date'])
#print (df.info())

low = sum(df['low'])
high = sum(df['high'])
df['price'] = (df['low'] + df['high'])/2

print (df['price'].describe())
print("var",df['price'].var())
print("codfficient of variation",df['price'].std()/df['price'].mean())
print("range",df['price'].max()-df['price'].min())
print("quartile deviation",df['price'].quantile(0.75)-df['price'].quantile(0.25))
print("kurtosis", df['price'].kurtosis())
print("skew",df['price'].skew())