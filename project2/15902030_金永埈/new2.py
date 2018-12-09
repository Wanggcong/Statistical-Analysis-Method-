import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

#The ability to distinguish between charges and gender in data.
data=pd.read_csv('D:/python/data.csv')
model=ols('charges ~ sex',data).fit()
anovat=anova_lm(model)
print(anovat)
print()

#The ability to tell the difference between charges and sex and smokers.
formula = 'charges~ sex + smoker'
anova_results=anova_lm(ols(formula,data).fit())
print(anova_results)

