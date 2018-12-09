# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:04:26 2018

@author: gym
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
 

df = pd.read_csv('000006.csv')
low = sum(df['low'])
high = sum(df['high'])
df['price'] = (df['low'] + df['high'])/2

plt.hist(df['price'],bins = int(np.sqrt(len(df['price']))), color = 'green', normed = True)
plt.show()

stats.probplot(df['price'],dist = "norm", plot =plt)
plt.show()


d_value = []
print(len(df['price']))
for i in range(len(df['price'])-1):
    #print(i)
    d_value.insert(i,df['price'][i+1]-df['price'][i])


plt.hist(d_value,bins = int(np.sqrt(len(d_value))), color = 'green', normed = True)
plt.show()

stats.probplot(d_value,dist = "norm", plot =plt)
plt.show()
    




 
