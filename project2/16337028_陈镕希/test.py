from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
data = pd.read_table("C://Users\XG\Desktop\datachange.txt", sep=',')
#print(data)
y = data.loc[:, 'charges'].as_matrix(columns=None)
y = np.array([y]).T
#print(y)
x = data.drop('charges', 1)
x = x.drop('region', 1)
x = x.drop('smoker',1)
x = x.drop('sex',1)
x = x.loc[0:].as_matrix(columns=None)
#print(x)
l = LinearRegression()
l.fit(x,y)
print(l.coef_)
print(l.predict([[50, 30.97, 3]]))
print(l.predict([[18, 31.92, 0]]))
print(l.predict([[18, 36.85, 0]]))
print(l.predict([[21, 25.8, 0]]))
print(l.predict([[61, 29.07, 0]]))
print(np.sqrt(np.mean((l.predict(x)-y)**2)))




#,header=None,encoding='gb2312',delim_whitespace=True,
#header=None:没有每列的column name，可以自己设定
#encoding='gb2312':其他编码中文显示错误
#delim_whitespace=True:用空格来分隔每行的数据
#index_col=0:设置第1列数据作为index

#print(l.score(x,y))
#print(np.mean((l.predict(x)-y)**2))