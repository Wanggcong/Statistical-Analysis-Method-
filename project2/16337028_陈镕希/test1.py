import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

data = pd.read_table("C://Users\XG\Desktop\data.txt", sep=',')
x = data.drop('age', 1)
x = x.drop('region', 1)
x = x.drop('smoker', 1)
x = x.drop('children', 1)
x = x.drop('bmi', 1)

anova_results = anova_lm(ols('charges~(sex)',x).fit())
print(anova_results)


#print(x)
#d1 = x[x['sex'] == 'male']['charges']
#d2 = x[x['sex'] == 'female']['charges']
#args = [d1,d2]
#print(d1)
#print(np.mean(d1))
#print(np.mean(d2))
#print(np.mean((d1-np.mean(d1))**2))
#print(np.mean((d2-np.mean(d2))**2))
#levene test
#print(args)
#w, p = stats.levene(*args)
#方差分析
#print(w, p)
#f, p=stats.f_oneway(*args)
#print(f, p)