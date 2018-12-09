import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns

adv_data=pd.read_csv("C:/Users/Administrator/PycharmProjects/untitled/.idea/data.csv")
#清洗不需要的数据
new_adv_data = adv_data.ix[:,[1,3,4,7]]
#得到我们所需要的数据集且查看其前几列以及数据形状
print(new_adv_data.head(),'\nShape:',new_adv_data.shape)

# 数据描述
print(new_adv_data.describe())
# 缺失值检验
print(new_adv_data[new_adv_data.isnull() == True].count())

new_adv_data.boxplot(sym = "o", # 异常点形状，参考marker
              vert = True, # 是否垂直
              whis = 1.5, # IQR，默认1.5， 也可以设置区间比如[5, 95], 代表强制上下边缘为数据95%和5%位置
              patch_artist = True, # 上下四分位框内是否填充，True会填充
              meanline = False, showmeans = True, # 是否有均值线及其形状
              showbox = True, # 是否显示箱线
              showcaps = True, # 是否显示边缘线
              showfliers = True, # 是否显示异常值
              notch = False, # 中间箱体是否缺口
              return_type = 'dict' # 返回类型为字典)
                     )
plt.savefig("boxplot.jpg")
plt.show()
##相关系数矩阵 r(相关系数) = x和y的协方差/(x的标准差*y的标准差) == cov（x,y）/σx*σy
# 相关系数0~0.3弱相关0.3~0.6中等程度相关0.6~1强相关
print(new_adv_data.corr())

# 通过加入一个参数kind='reg'，seaborn可以添加一条最佳拟合直线和95%的置信带。
sns.pairplot(new_adv_data, x_vars=['age','bmi','children'], y_vars='charges', height=7, aspect=0.8,kind = 'reg')
plt.savefig("pairplot.jpg")
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(new_adv_data.ix[new_adv_data.ix[:,0]<1333,:3], new_adv_data.charges, train_size=1333,random_state=0)

model = LinearRegression()

model.fit(X_train, Y_train)

a = model.intercept_  # 截距

b = model.coef_  # 回归系数

print("最佳拟合线:截距", a, ",回归系数：", b)

# R方检测
# 决定系数r平方
# 对于评估模型的精确度
# y误差平方和 = Σ(y实际值 - y预测值)^2
# y的总波动 = Σ(y实际值 - y平均值)^2
# 有多少百分比的y波动没有被回归拟合线所描述 = SSE/总波动
# 有多少百分比的y波动被回归线描述 = 1 - SSE/总波动 = 决定系数R平方
# 对于决定系数R平方来说1） 回归线拟合程度：有多少百分比的y波动刻印有回归线来描述(x的波动变化)
# 2）值大小：R平方越高，回归模型越精确(取值范围0~1)，1无误差，0无法完成拟合
score = model.score(X_test, Y_test)

print(score)

# 对线性回归进行预测

Y_pred = model.predict(new_adv_data.ix[1333:1337,:3])

print(new_adv_data.ix[1333:1337,:3])
print(Y_pred)

plt.plot(range(len(Y_pred)), Y_pred, 'b', label="predict")
# 显示图像
plt.savefig("predict.jpg")
plt.show()

