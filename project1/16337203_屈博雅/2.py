import numpy as np
import statsmodels.api as sm
import pylab
import csv
import math
import copy
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from PIL import Image  
import scipy.stats as stats
import pandas as pd
from statsmodels.graphics.api import qqplot

def drawHist(data0,size,num):
    mean = np.mean(data0)
    #标准差为1，反应数据集中还是分散的值  
    sigma = np.std(data0,ddof=1)  
    x = data0

    fig,ax0 = plt.subplots(nrows=1,figsize=(9,6))  
    #fig,(ax0,ax1) = plt.subplots(nrows=2,figsize=(9,6))  
    #第二个参数是柱子宽一些还是窄一些，越大越窄越密  
    n, bins, patches = ax0.hist(np.sort(x), num, normed=1,histtype='bar', facecolor='blue', alpha=0.5)
    y = mlab.normpdf(bins, mean, sigma)
    #print('n=',n)
    '''
    normpdf：正态概率密度函数
    Y = normpdf(X,mu,sigma)
    mu：均值
    sigma：标准差
    Y：正态概率密度函数在x处的值
    '''  
    plt.plot(bins, y, 'r--')  
    ##pdf概率分布图，一万个数落在某个区间内的数有多少个  
    ax0.set_title('pdf')  
    #plt.subplots_adjust(left=0.15) 
    plt.show()

def drawQQ(data,size):
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    fig = qqplot(data, line='q', ax=ax, fit=True)
    plt.show()

csv_reader=csv.reader(open('C:\\Users\\quby\\homework\\tjhw1\\data_selected\\000006.csv',encoding='utf-8'))

V=[]
size=0
for row in csv_reader:
    V.append(row)
    size+=1

#print(V[0][3])
#print(V[0][4])
data0_=np.zeros((size-1,1))
data3_=np.zeros((size-2,1))

data0=[]
for i in range(size-1):
    x=(float(V[i+1][3])+float(V[i+1][4]))/2
    data0.append(x)
    data0_[i]=x

drawHist(data0,size,50)
drawQQ(data0_,size-1)

data3=[]
for i in range(1,size-1):
    x=data0[i]-data0[i-1]
    data3.append(x)
    data3_[i-1]=x

drawHist(data3,size-1,300)
drawQQ(data3_,size-2)

