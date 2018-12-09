import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

data = pd.read_table('E:\Study\data.txt', sep=',')
mat_data = pd.DataFrame({
    'age': data['age'],
    'bmi': data['bmi'],
   'children': data['children'],
    'charges': data['charges']
})
#作出charges与三个定量数值的皮尔森系数矩阵
mat_data_corr = mat_data.corr('pearson')
mat_data_corr.to_csv("Quantitative Pearson.csv", encoding="gb2312")
print(mat_data_corr)
#画出三个定量数值与charges相关性的线性拟合图
sns.pairplot(mat_data, x_vars=['age', 'bmi', 'children'], y_vars='charges', height=5, aspect=0.8, kind='reg')
plt.savefig("Linear regression fitting.png")
plt.show()
#丢掉1338条数据中最后5条，留下前面的1333条
mat_data1 = mat_data
for i in range(5):
    mat_data1 = mat_data1.drop(1333 + i)
#利用sklearn模块构建线性回归方程，求得a为截距即b0，b_为其他三个定量数值的系数
x_train, tm1, y_train, tm2 = train_test_split(mat_data1[['age', 'bmi', 'children']], mat_data1['charges'],
                                                    test_size=0)
model = LinearRegression()
model.fit(x_train, y_train)
a = model.intercept_
b_ = model.coef_
#输出线性回归方程
print("向量b:")
print("b0:%f  b1:%f  b2:%f  b3:%f" % (a, b_[0], b_[1], b_[2]))
print("则拟合的线性回归方程：")
print("charges = %f + %f * age + %f * bmi + %f * children" % (a, b_[0], b_[1], b_[2]))
print("\n\n")
#取最后5条数据作为测试集进行数据的预测，得到5个预测值
x_test = mat_data[['age', 'bmi', 'children']]
x_test = x_test.ix[1333:1337]
y_test = mat_data['charges']
y_test = y_test.ix[1333:1337]
y_pre = model.predict(x_test)
print("最后五个数据的预测值：")
for i in range(5):
    print("%d: %f" % (i+1333, y_pre[i]))

#计算MSE
def calculatemse(x1, x2, x3, y, a, b):
    in_bracket = []
    for i in range(len(x1)):
        num = y[i] - (a + b[0] * x1[i] + b[1] * x2[i] + b[2] * x3[i])
        num = pow(num, 2)
        in_bracket.append(num)

    all_sum = sum(in_bracket)
    mse = all_sum / len(x1)
    return mse
#利用书上的公式求得5个预测值的置信度为95%的置信区间
mse = calculatemse(x_train['age'], x_train['bmi'], x_train['children'], y_train, a, b_)
xxx = np.array(x_train)
xxx = np.dot(xxx.transpose(), xxx)
xxx = np.linalg.inv(xxx)
t = stats.t.isf(0.05/2, 1333 - 4)
print("\n\n最后五个数据的预测值置信区间：")
for i in range(5):
    s = np.array(x_test.iloc[i])
    temp = np.dot(s, xxx)
    s_t = np.transpose([s])
    temp = np.dot(temp, s_t)
    num = 1 + temp
    print("[%f,%f]" % (y_pre[i] - t * math.sqrt(mse * num),  y_pre[i] + t * math.sqrt(mse * num)))
print("\n\n")
#对charges和性别sex的单因素方差分析
print("对charges和性别sex的单因素方差分析：")
model2 = ols('charges~sex', data).fit()
anovat2 = anova_lm(model2)
print(anovat2)

print("\n\n")
#对charges和性别sex与是否吸烟smoker的双因素方差分析
print("对charges和性别sex与是否吸烟smoker的双因素方差分析：")
model3 = ols('charges~sex + smoker', data).fit()
anovat3 = anova_lm(model3)
print(anovat3)