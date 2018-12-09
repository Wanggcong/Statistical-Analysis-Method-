
from PIL import Image
from pylab import *
import numpy as np
import matplotlib
from skimage import transform,data
import matplotlib.pyplot as plt
import cv2
import matplotlib.cbook as cbook
import matplotlib.cm as cm
import scipy.misc
import os
import pandas as pd
import csv
import xlwt
import math
import copy
from pydoc import help
from datetime import datetime
from datetime import timedelta
from itertools import chain

def pca_image(size_block0,size_block1,num_val,row,col,im2):
    shape0=size_block0*size_block1
    shape1=int((row/size_block0)*(col/size_block1))
    print('shape0=',(size_block0,size_block1))
    print('shape1=',((row/size_block0),(col/size_block1)))
    print('shape=',(shape0,shape1))
    m=0
    Data = np.zeros((shape0,shape1)) 
    for i in range(0,row,size_block0):
        for j in range(0,col,size_block1):
            block = im2[i:i+size_block0,j:j+size_block1]
            Data[:,m] = block.reshape(size_block0*size_block1)
            m = m+1
    print('block=',block.shape)
    print('shape=',Data.shape)
    x_m_i=np.mean(Data, axis=0) # axis=0，计算每一列的均值
    Data1=np.array(Data, dtype='float64')
    mean_Data1 = Data1.mean(axis=0)
    Data1 = Data1 - mean_Data1

    c=np.cov(Data1)#不知道要不要T
    val,vec = np.linalg.eigh(c) 
    val = val[::-1]
    for i in range(shape0):
        vec[i,:] = vec[i,:][::-1]
    print('vec=',vec.shape)
    #重构图像
    vec_new = vec[:,0:num_val]  # 取前k个特征向量                              
    #计算所取特征值贡献率
    rata_sum = np.sum(val[:num_val])/np.sum(val)
    print('选取%g个特征值的贡献率为%g'%(num_val,rata_sum))
    y=np.dot(vec_new.T,Data)
    #print(y.shape)
    Data2=np.dot(vec_new,y)
    mean_Data2 = Data.mean(axis=0)
    Data2 = Data2 + mean_Data2
    
    m=0
    out = np.zeros(im2.shape) 
    for i in range(0,row,size_block0):
        for j in range(0,col,size_block1):
            block1 = Data2[:, m].reshape(size_block0, size_block1)
            out[i:i+size_block0, j:j+size_block1] = block1
            m = m+1
    print('block1=',block1.shape)
    return out


# 加载图像
im1 = cv2.imread("lena_gray.bmp",0)
#im2 = cv2.resize(im1, (256,256), interpolation=cv2.INTER_CUBIC)
im2=im1
scipy.misc.imsave('img0.bmp', im2)
#im2=im1
im2=np.array(im2, dtype='float64')
row,col = im2.shape 
#num_val = 1  #取前num_val个特征值
#size_block = 4
#out=pca_image(size_block,num_val,row,col,im2)#函数参数
size_block0=4
size_block1=4
out1=pca_image(size_block0,size_block1,int(size_block0*size_block1/2),row,col,im2)
out2=pca_image(size_block0,size_block1,int(size_block0*size_block1/8),row,col,im2)
out3=pca_image(size_block0,size_block1,int(size_block0*size_block1/32),row,col,im2)
scipy.misc.imsave('C:/Users/quby/homework/tjhw3/压缩照片对比/pca_2_im_512_img1_4_4.bmp', out1)
scipy.misc.imsave('C:/Users/quby/homework/tjhw3/压缩照片对比/pca_2_im_512_img2_4_4.bmp', out2)
scipy.misc.imsave('C:/Users/quby/homework/tjhw3/压缩照片对比/pca_2_im_512_img3_4_4.bmp', out3)
fig=plt.figure()
fig.suptitle('show picture')

ax=fig.add_subplot(221)
ax.imshow(im2, cmap=cm.gray)
#子图表的标题
ax.set_title('the original image')
ax.axis('off')

ax=fig.add_subplot(222)
ax.imshow(out1, cmap=cm.gray)
#子图表的标题
ax.set_title('2')
ax.axis('off')

ax=fig.add_subplot(223)
ax.imshow(out2, cmap=cm.gray)
#子图表的标题
ax.set_title('8')
ax.axis('off')

ax=fig.add_subplot(224)
ax.imshow(out3, cmap=cm.gray)
#子图表的标题
ax.set_title('32')
ax.axis('off')

plt.show()
