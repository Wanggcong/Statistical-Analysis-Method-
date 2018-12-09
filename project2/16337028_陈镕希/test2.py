import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


data = pd.read_table("C://Users\XG\Desktop\data.txt", sep=',')
x = data.drop('age', 1)
x = x.drop('region', 1)
x = x.drop('children', 1)
x = x.drop('bmi', 1)
anova_results = anova_lm(ols('charges~(sex)+(smoker)',x).fit())
print(anova_results)