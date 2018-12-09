# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:23:29 2018

@author: gym
"""

import pandas as pd
import numpy as np

df = pd.read_csv('000012.csv')
low = sum(df['low'])
high = sum(df['high'])
df['price'] = (df['low'] + df['high'])/2


del df['open']
del df['close']
del df['high']
del df['low']
del df['code']
print("Pearson")
print(df.corr())
print("\n")
print("Spearman")
print(df.corr('spearman'))
