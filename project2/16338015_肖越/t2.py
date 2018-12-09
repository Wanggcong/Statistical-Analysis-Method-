from pandas import DataFrame
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
np.set_printoptions(suppress =True)

f=pd.read_csv("C:/Users/Administrator/PycharmProjects/untitled/.idea/data.csv")
a= DataFrame(f)
a.head()

model = ols('charges ~ sex',a).fit()
anovat = anova_lm(model)
print(anovat)
print(model.summary())

modell = ols('charges ~ sex+smoker',a).fit()
temp = anova_lm(modell)
print(temp)
print(modell.summary())