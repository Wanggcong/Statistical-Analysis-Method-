import csv
import math
import copy
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pydoc import help
from scipy.stats.stats import pearsonr
from scipy.stats.stats import spearmanr
csv_reader=csv.reader(open('C:\\Users\\quby\\homework\\tjhw1\\data_selected\\000012.csv',encoding='utf-8'))
#csv_reader=csv.reader(open('C:\\Users\\quby\\homework\\tjhw1\\data_selected\\test.csv',encoding='utf-8'))
#data1=np.zeros((4380,7))
V=[]
size=0
for row in csv_reader:
    V.append(row)
    size+=1
    #print(row)
#print('V=',V)
#print(float(V[1][1]))

#求出每日股价data0
data0=[]
data1=[]
for i in range(size-1):
    x=(float(V[i+1][3])+float(V[i+1][4]))/2
    y=float(V[i+1][5])
    data0.append(x)
    data1.append(y)
#print(np.corrcoef(data0, data1)[0, 1])
pearsonr=pearsonr(data0, data1)
print('pearsonr=',pearsonr[0])

spearmanr=spearmanr(data0, data1)
print('spearsonr=',spearmanr[0])