
import os
import pandas as pd
import csv
import xlwt
import math
import copy
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pydoc import help
from scipy.stats.stats import pearsonr
from scipy.stats.stats import spearmanr
from datetime import datetime
from datetime import timedelta
from itertools import chain


def add_date_price(datas):
    price = []
    # 按条件修改two
    for i in range(datas.shape[0]):
        x=0.5*(datas['high'][i]+datas['low'][i])
        price.append(x)
    datas.insert(7,'price', price)
    '''
    datas['price']=None
    for i in range(datas.shape[0]):
        datas['price'][i]=0.5*(datas['high'][i]+datas['low'][i])
    #会出现warning，因为顺序不对，应该先建立要插入的数组，再插入，不是先建立class里的数组，再赋值
    '''
    #print(datas)
    return datas

def pearsonr_spearmanr_out(csv1,csv2):
    #筛选时间一样的，搞到股价信息，分析相关性
    data_try=pd.merge(csv1,csv2,on='date')
    #print(data_try.shape)
    pear=pearsonr(data_try['price_x'], data_try['price_y'])
    #print('pearsonr=',pear[0])
    spear=spearmanr(data_try['price_x'], data_try['price_y'])
    #print('spearmanr=',spear[0])
    return pear, spear

if __name__ == '__main__':
    datas=[]
    for info in os.listdir('C:\\Users\\quby\\homework\\tjhw1\\data_selected'):
        domain = os.path.abspath(r'C:\\Users\\quby\\homework\\tjhw1\\data_selected') #获取文件夹的路径
        info = os.path.join(domain,info) #将路径与文件名结合起来就是每个文件的完整路径  
        data = pd.read_csv(info)
        datas.append(data)

    size_=100
    #每日股价处理，接下来任务：筛选两组时间
    for i in range(size_):
        datas[i]=add_date_price(datas[i])
        #print('add_price_datas=',datas[i].shape)
   
    p=np.zeros((size_,size_))
    s=np.zeros((size_,size_))
    Pearsonrs=[]
    Spearmanrs=[]
    
    PP, SS =pearsonr_spearmanr_out(datas[0],datas[1])
    print(PP)
    print(SS)

    for i in range(size_):
        for j in range(size_):
            Pea, Spea =pearsonr_spearmanr_out(datas[i],datas[j])
            p[i][j]=abs(Pea[0])
            s[i][j]=abs(Spea[0])
            Pearsonrs.append(Pea)
            Spearmanrs.append(Spea)

    '''
    print('p=',p)
    print('s=',s)
    print('Pearsonrs=',Pearsonrs)
    print('Spearmanrs=',Spearmanrs)
    '''
    '''
    np.savetxt('S_t0.txt',s)
    np.savetxt('P_t0.txt',p)
    np.savetxt('S_t_all.txt',Spearmanrs)
    np.savetxt('P_t_all.txt',Pearsonrs)
    '''

    book = xlwt.Workbook()#新建一个excel
    sheet1 = book.add_sheet('p_0_sheet')#添加一个sheet页
    sheet2 = book.add_sheet('s_0_sheet')#添加一个sheet页
    sheet3 = book.add_sheet('p_all_sheet')#添加一个sheet页
    sheet4 = book.add_sheet('s_all_sheet')#添加一个sheet页
    sheet5 = book.add_sheet('p_all_p_10_sheet')#添加一个sheet页
    sheet6 = book.add_sheet('p_all_s_10_sheet')#添加一个sheet页
    sheet7 = book.add_sheet('s_all_p_10_sheet')#添加一个sheet页
    sheet8 = book.add_sheet('s_all_s_10_sheet')#添加一个sheet页
    row = 0#控制行
    for stu in p:
        col = 0#控制列
        for s_ in stu:#再循环里面list的值，每一列
            sheet1.write(row,col,s_)
            col+=1
        row+=1
    book.save('2.xls')#保存到当前目录下

    row = 0#控制行
    for stu in s:
        col = 0#控制列
        for s_x in stu:#再循环里面list的值，每一列
            sheet2.write(row,col,s_x)
            col+=1
        row+=1
    book.save('2.xls')#保存到当前目录下

    row = 0#控制行
    for stu in Pearsonrs:
        col = 0#控制列
        for s_ in stu:#再循环里面list的值，每一列
            sheet3.write(row,col,s_)
            col+=1
        row+=1
    book.save('2.xls')#保存到当前目录下

    row = 0#控制行
    for stu in Spearmanrs:
        col = 0#控制列
        for s_ in stu:#再循环里面list的值，每一列
            sheet4.write(row,col,s_)
            col+=1
        row+=1
    book.save('2.xls')#保存到当前目录下
    
    #数据经过人工处理，暂时
    s_all_pos= np.array([6285,  2250,  23, 3185, 3754, 3493,  3684,  631, 6206,  8409])
    ij_s0_pos= np.array([(62, 85),  (22, 50),  (0, 23), (31, 85), (37, 54), (34, 93),  (36, 84),  (6, 31), (62, 6),  (84, 9)])
    # 0 6 9 22 23 31 34 36 37 50 54  62 84 85 93    
    p_all_pos= np.array([4580, 1425, 4384, 7484, 1037, 1697, 121, 662, 113, 1321])
    ij_p0_pos= np.array([[45, 80], [14, 25], [43, 84], [74, 84], [10, 37], [16, 97], [1, 21], [6, 62], [1, 13], [13, 21]])
    # 1 6 10 13 14 16 21 25 37 43 45 62 74 80 84 97  
    #存放pea算法求出的十对的两种p值
    pea_10_pea_pvalue=[]
    pea_10_spea_pvalue=[]
    pea_10_p=[]
    pea_10_s=[]

    #存放spea算法求出的十对的两种p值
    spea_10_spea_pvalue=[]
    spea_10_pea_pvalue=[]
    spea_10_p=[]
    spea_10_s=[]
    sum1=0
    sum2=0
    sum1_abs=0
    sum2_abs=0
    for i in p_all_pos:
        #print(Pearsonrs[i][1])
        x=Pearsonrs[i][1]
        y=Pearsonrs[i]
        pea_10_pea_pvalue.append(x)
        pea_10_p.append(y)
        x=Spearmanrs[i][1]
        y=Spearmanrs[i]
        pea_10_spea_pvalue.append(x)
        pea_10_s.append(y)
 
    for i in s_all_pos:
        x=Spearmanrs[i][1]
        y=Spearmanrs[i]
        spea_10_spea_pvalue.append(x)  
        spea_10_s.append(y)
        x=Pearsonrs[i][1]
        y=Pearsonrs[i]
        spea_10_pea_pvalue.append(x)  
        spea_10_p.append(y)

    print('Spearmanrs:')
    for xxx in range(10):
        i=datas[ij_s0_pos[xxx][0]]['code'][0]
        j=datas[ij_s0_pos[xxx][1]]['code'][0]
        print('第 %d 对股票是( %d， %d ) ' % (xxx+1,i,j))

    print('Pearsonrs:')
    for xxx in range(10):
        i=datas[ij_p0_pos[xxx][0]]['code'][0]
        j=datas[ij_p0_pos[xxx][1]]['code'][0]
        print('第 %d 对股票是( %d， %d ) ' % (xxx+1,i,j))


    print('pea_10_pea_pvalue=',pea_10_pea_pvalue)
    print('pea_10_spea_pvalue=',pea_10_spea_pvalue)

    print('spea_10_pear_pvalue=',spea_10_pea_pvalue)
    print('spea_10_spear_pvalue=',spea_10_spea_pvalue)
    
    '''
    #所需十对的p值
    pea_10_pvalue= [0.9849317585223375, 0.96621560465683753, 0.95647843421478063, 0.94526373334347769, 0.91267462875677452, 0.0, 0.0, 0.0, 0.0, 0.0]
    spea_10_pvalue= [0.98059952399803763, 0.97922531724940554, 0.96482347586905515, 0.96119318211375626, 0.93131916837179762, 0.0, 0.0, 0.0, 0.0, 0.0]
    #pvalue平均值为
    a1_p= 0.476556415949
    a2_s= 0.48171606676
    '''
    
    row = 0#控制行
    for stu in pea_10_p:
        col = 0#控制列
        for s_ in stu:#再循环里面list的值，每一列
            sheet5.write(row,col,s_)
            col+=1
        row+=1
    book.save('2.xls')#保存到当前目录下

    row = 0#控制行
    for stu in pea_10_s:
        col = 0#控制列
        for s_ in stu:#再循环里面list的值，每一列
            sheet6.write(row,col,s_)
            col+=1
        row+=1
    book.save('2.xls')#保存到当前目录下
       
    row = 0#控制行
    for stu in spea_10_p:
        col = 0#控制列
        for s_ in stu:#再循环里面list的值，每一列
            sheet7.write(row,col,s_)
            col+=1
        row+=1
    book.save('2.xls')#保存到当前目录下

    row = 0#控制行
    for stu in spea_10_s:
        col = 0#控制列
        for s_ in stu:#再循环里面list的值，每一列
            sheet8.write(row,col,s_)
            col+=1
        row+=1
    book.save('2.xls')#保存到当前目录下
    '''
    #1.求出对应的五对接近1的+5对接近0的股票可能数值，
    c1=list(chain(*s))
    d1=sorted(c1)
    print(d1[:10])
    print(d1[-110:])

    c2=list(chain(*p))
    d2=sorted(c2)
    print(d2[:10])
    print(d2[-110:])
    '''

    '''
    s
    小的
    [0.00036783203180637455, 0.0003678320318063746, 
    0.00039880469825196466, 0.00039880469825196471, 
    0.00067604915633986929, 0.00067604915633986929, 
    0.00074187251241837713, 0.00074187251241837713, 
    0.0013241252559623492, 0.0013241252559623492]

    大的
    [0.9308496459665726, 0.93084964596657271, 
    0.93110307854567598, 0.93110307854567609, 
    0.93602510045417409, 0.93602510045417409, 
    0.9431301023573373, 0.94313010235733741, 
    0.96159272894408754, 0.96159272894408765]

    P:
    小的
    [0.0002854860231784521, 0.0002854860231784521, 
    0.00064768171908101153, 0.00064768171908101153, 
    0.00082758034325261661, 0.00082758034325261661, 
    0.0010438976200018892, 0.0010438976200018892, 
    0.0016803144859775781, 0.0016803144859775781]

    大的
    [0.906159711693867, 0.906159711693867, 
    0.91506868146878262, 0.91506868146878262, 
    0.927051782130761, 0.927051782130761, 
    0.94644810496111309, 0.94644810496111309, 
    0.94948463891436374, 0.94948463891436374]

    #人工处理（去重、去1）得到上面的最终结果
    '''

    
    '''
    #2.这一块用于求出十对所需股票的位置，得到两组十对
    s_10=np.array([0.00036783203180637455, 
                   0.0003678320318063746, 
                   0.00039880469825196466, 
                   0.00039880469825196471, 
                   0.00067604915633986929, 
                   0.00074187251241837713,  
                   0.0013241252559623492,
                        0.9308496459665726, 
                        0.93084964596657271, 
                        0.93110307854567598, 
                        0.93110307854567609, 
                        0.93602510045417409, 
                        0.9431301023573373, 
                        0.94313010235733741,
                        0.96159272894408754, 
                        0.96159272894408765])

    p_10=np.array([0.0002854860231784521, 
                    0.00064768171908101153, 
                    0.00082758034325261661,  
                    0.0010438976200018892,  
                    0.0016803144859775781, 
                    0.906159711693867,  
                    0.91506868146878262, 
                    0.927051782130761,
                    0.94644810496111309,  
                    0.94948463891436374])

    c1=list(chain(*s))
    #d1=sorted(c1)
    #print(d1[:10])
    #print(d1[-110:])

    c2=list(chain(*p))
    #d2=sorted(c2)
    #print(d2[:10])
    #print(d2[-110:])
    
    def get_i_j(x,size_):
        i=x//size_
        j=x%size_
        return list((i,j))
    
    num_s=[]
    ij_num_s=[]
    for i in s_10:
        x=c1.index(i)
        num_s.append(x)
        ij_num_s.append(get_i_j(x,size_)) 
    
    print('num_s=',num_s)
    print('ij_s=',ij_num_s)


    num_p=[]
    ij_num_p=[]
    for i in p_10:
        x=c2.index(i)
        num_p.append(x)
        ij_num_p.append(get_i_j(x,size_)) 
    
    print('num_p=',num_p)
    print('ij_p=',ij_num_p)
    '''
    '''
    #2.结果
    num_s= [6285, 8562, 2250, 5022, 23, 3185, 3754, 3493, 9334, 3684, 8436, 631, 6206, 662, 8409, 984]
    ij_s= [[62, 85], [85, 62], [22, 50], [50, 22], [0, 23], [31, 85], [37, 54], [34, 93], [93, 34], [36, 84], [84, 36], [6, 31], [62, 6], [6, 62], [84, 9], [9, 84]]
    num_p= [4580, 1425, 4384, 7484, 1037, 1697, 121, 662, 113, 1321]
    ij_p= [[45, 80], [14, 25], [43, 84], [74, 84], [10, 37], [16, 97], [1, 21], [6, 62], [1, 13], [13, 21]]
    
    #处理后
    num_s= [6285,  2250,  23, 3185, 3754, 3493,  3684,  631, 6206,  8409]
    ij_s= [[62, 85],  [22, 50],  [0, 23], [31, 85], [37, 54], [34, 93],  [36, 84],  [6, 31], [62, 6],  [84, 9]]
    # 0 6 9 22 23 31 34 36 37 50 54  62 84 85 93    
    num_p= [4580, 1425, 4384, 7484, 1037, 1697, 121, 662, 113, 1321]
    ij_p= [[45, 80], [14, 25], [43, 84], [74, 84], [10, 37], [16, 97], [1, 21], [6, 62], [1, 13], [13, 21]]
    # 1 6 10 13 14 16 21 25 37 43 45 62 74 80 84 97  
    '''