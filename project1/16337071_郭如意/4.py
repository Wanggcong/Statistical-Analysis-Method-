# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:38:38 2018

@author: gym
"""

import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr
import os

flist = os.listdir('C:\Users\gym\Desktop\data_selected')

#print(flist)
s = [[],[]]
for i in range(len(flist)):
    
    if flist[i] == '4.py':
        break
    if flist[i] == 'test.py':
        break
    print(flist[i])
    
    for j in range(len(flist)):
        
        if flist[j] == '4.py':
            break
        if flist[j] == 'test.py':
            break
        if i == j:
            continue
        #print(flist[j])
        price1 = []
        price2 = []
       
        df1 = pd.read_csv(flist[i])  
        df2 = pd.read_csv(flist[j])   
        
        df1['price'] = (df1['low'] + df1['high'])/2    
        df2['price'] = (df2['low'] + df2['high'])/2
    
        #print(df1[['price']])
        #print( df1['date'][0])
        #print (df2['date'][0])
        for x in df1['date']:
            for y in df2['date']:
                if x == y:
                    #print(x)
                    #print("a")
                    index_1 = df1[df1.date == x].index.tolist()
                    index_2 = df2[df2.date == x].index.tolist()
                    #print(index_1)
                    price1.append(df1['price'][index_1[0]])
                    #print(df1['price'][index_1])
                    price2.append(df2['price'][index_2[0]])
        #print(price1)
        
        M,P = pearsonr(price1,price2)
        
        s[0].append(M)
        s[1].append(P)
        #print(s)

        #print("Spearman")
        #print(new_df.corr('spearman'))
print("Pearson: ")
print(s)
x = []
y = []
for ii in range(5):
    x.append(s[0].index(max(s[0])))
    y.append(s[1][x[ii]])

print(y)

x1 = []
y1 = []
for ii in range(5):
    x1.append(s[0].index(min(s[0])))
    y1.append(s[1][x1[ii]])

print(y1)


