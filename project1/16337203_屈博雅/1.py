import csv
import math
import copy
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

csv_reader=csv.reader(open('C:\\Users\\quby\\homework\\tjhw1\\data_selected\\000001.csv',encoding='utf-8'))
V=[]
size=0
for row in csv_reader:
    V.append(row)
    size+=1

#求出每日股价data0
data0=[]
for i in range(size-1):
    x=(float(V[i+1][3])+float(V[i+1][4]))/2
    data0.append(x)


#求出平均值
average=np.mean(data0)
print('日均值=',average)

#求出中位数
median=np.median(data0)
print('中位数=',median)

#0.25分位数
percentile1=np.percentile(data0,25)
print('0.25分位数=',percentile1)

#0.75分位数
percentile2=np.percentile(data0,75)
print('0.75分位数=',percentile2)

#方差
var = np.var(data0,ddof=1)
print('方差=',var)

#标准差
std = var**0.5
#temp = np.std(data0,ddof=1)
print('标准差=',std)

#变异系数
cv = std/average
print('变异系数=',cv)

#极差
range_ = np.ptp(data0)
print('极差=',range_)

#四分位极差
r=percentile2-percentile1
print('四分位极差=',r)

#偏度
n = size-1
g1 =n/((n-1)*(n-2))*(1/(std**3))*np.sum((data0 - average) ** 3) #计算偏斜度
print('偏度=',g1)

#峰度
g2 = n*(n+1)/((n-1)*(n-2)*(n-3))*(1/(std**4))*np.sum((data0 - average) ** 4)-3*((n-1)**2)/((n-2)*(n-3)) #计算峰度
print('峰度=',g2)


