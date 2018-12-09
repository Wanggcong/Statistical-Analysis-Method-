# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:44:37 2018

@author: pro
"""
import numpy as np

age=[]
bmi=[]
children=[]
charges=[]#因变量

#读取数据
def loadDataSet():
    f  = open('data.txt','r')
    f.readline()
    for lines in f:
        readin = lines.strip('\n').split(',')
        age.append(float(readin[0]))
        bmi.append(float(readin[2]))
        children.append(float(readin[3]))
        charges.append(float(readin[6]))     
    f.close()

def regr_analysis():
    xMat=[]
    for i in range(1333):
        xMat.append([1,age[i], bmi[i], children[i]])
    xMat = np.mat(np.array(xMat))
    yMat = np.mat(np.array([charges[0:1333]]).T)
    
    xTx = xMat.T * xMat
    beta = np.array(xTx.I * (xMat.T * yMat))

    SSE = 0   #残差平方和
    for i in range(1333):
        pred_y = beta[0] + beta[1]*age[i] + beta[2]*bmi[i] + beta[3]*children[i]
        SSE = SSE + (pred_y - charges[i])**2
    
    sigma_2 = SSE/(1333-5)    #方差
   
    con_interval = np.ones((1, 2))
    t_value = 1.960

    pred_y = 0   
    for i in range(1333, 1338):
        arr = np.array([1, age[i], bmi[i], children[i]])
        pred_y = beta[0] + beta[1]*age[i] + beta[2]*bmi[i] + beta[3]*children[i]
        #print(arr.T@np.array(xTx.I)@arr)
        temp1 = pred_y - t_value*np.sqrt(sigma_2*(1 + arr.T@np.array(xTx.I)@arr))
        temp2 = pred_y + t_value*np.sqrt(sigma_2*(1 + arr.T@np.array(xTx.I)@arr))
        con_interval[0][0] = temp1
        con_interval[0][1] = temp2
        print('预测值为', pred_y)
        print('置信区间为', con_interval)
    
loadDataSet()
regr_analysis()