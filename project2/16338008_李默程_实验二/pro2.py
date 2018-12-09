import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import statsmodels.sandbox.regression.predstd as pred

data = pd.read_csv('data.txt')#读取文件

#线性回归函数
train_data = data.iloc[:1333, :]#训练集
test_data = data.iloc[1333:, :]#测试集

clf = linear_model.LinearRegression()#回归函数
clf.fit(train_data.iloc[:, [0, 2, 3]], train_data.iloc[:, 6])#拟合
y_pred = clf.predict(test_data.iloc[:, [0, 2, 3]], ) #对测试集预测
print('回归系数，常量')
print(clf.coef_, clf.intercept_)#回归系数
print('预测结果：')
print(y_pred)
print('真实结果：')
print(np.array(test_data.iloc[:, 6]))

#绘图
sns.pairplot(train_data, x_vars=['age', 'bmi', 'children'], y_vars='charges', size=7, aspect=0.8, kind='reg')
plt.show()

#计算置信区间
model = ols('charges~age+children+bmi', data).fit()#y, x
print('置信区间:')
_, pre_lower, pre_upper = pred.wls_prediction_std(model, alpha=0.05)
pre = np.array([pre_lower[1333:], pre_upper[1333:]]).T
print(pre)



#第二题
print('显著性分析:')
print('费用与性别的相关性')
model2 = ols('charges ~ sex', data).fit()
print(anova_lm(model2))

print('费用与性别和是否吸烟的相关性')
model3 = ols('charges ~ sex + smoker', data).fit()
print(anova_lm(model3))
pass

