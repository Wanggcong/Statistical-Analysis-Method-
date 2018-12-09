# 통계 문제1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
from pandas import DataFrame,Series
from sklearn.linear_model import LinearRegression
from scipy import stats

data=pd.read_csv('D:/python/data.csv')
a=data[0:1333]
x=a[['age','bmi','children']]
y=a[['charges']]
lrModel=LinearRegression() #建模
lrModel.fit(x,y)        #训练模型
print(np.c_[np.array(['age','bmi','children']).reshape((3,1)),lrModel.coef_.reshape((3,1))])   #查看系数
print(lrModel.intercept_)    #查看截距
print('Linear regression equation：')
print('y=',lrModel.intercept_[0],'+',lrModel.coef_[0][0],'* age','+',lrModel.coef_[0][1],'* bmi','+',lrModel.coef_[0][2],'* children')
y_pred=lrModel.predict([[50,30.970,3],[18,31.920,0],[18,36.850,0],[21,25.800,0],[61,29.070,0]]) #预测
print()
print('Prediction results：')
print(y_pred)
print()

plt.figure()    #画出预测和实际图
plt.plot(range(len(y_pred)),y_pred,'b',label="predict")
y_test=[10600.54830,2205.98080,1629.83350,2007.94500,29141.36030]
plt.plot(range(len(y_pred)),y_test,'r',label="test")
plt.legend(loc="upper right")
plt.xlabel('test cases')
plt.ylabel('charges')
plt.show()
#95%的置信区间
def ci_t(data, confidence=0.95):
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)
    sample_size = len(data)
    alpha = 1 - confidence
    t_score = scipy.stats.t.isf(alpha / 2, df=(sample_size - 1))

    ME = t_score * sample_std / np.sqrt(sample_size)
    lower_limit = sample_mean - ME
    upper_limit = sample_mean + ME

    return lower_limit, upper_limit

X1=[10600.54830,2205.98080,1629.83350,2007.94500,29141.36030]
print('95% confidence interval：')
print(ci_t(X1))
