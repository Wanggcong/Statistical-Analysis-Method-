# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:13:20 2018

@author: pro
"""
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

file = pd.read_table('data.txt', sep = ',')
data = file.drop('age', 1)
data = data.drop('bmi', 1)
data = data.drop('children', 1)
data0 = data.drop('region', 1)
data1 = data0.drop('smoker', 1)
    
def var_analysis(data, model):
    anova_results = anova_lm(ols(model, data).fit())
    print(anova_results)

#不同性别对个人医疗费用是否有显著差异
var_analysis(data, 'charges ~ C(sex)')

#不同性别、是否吸烟两个因素对个人医疗费用是否有显著差异
var_analysis(data0, 'charges ~ sex + smoker')