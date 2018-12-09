
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

def pca_image(size_block0,size_block1,row,col,im2,r):
    shape0=size_block0*size_block1
    shape1=int((row/size_block0)*(col/size_block1))
    print('shape0=',(size_block0,size_block1))
    print('shape1=',((row/size_block0),(col/size_block1)))
    print('shape=',(shape0,shape1))

    Data = np.zeros((shape0,shape1)) 
    m=0
    for i in range(0,row,size_block0):
        for j in range(0,col,size_block1):
            block = im2[i:i+size_block0,j:j+size_block1]
            Data[:,m] = block.reshape(size_block0*size_block1)
            m = m+1
    print('block=',block.shape)
    print('shape=',Data.shape)
    u,s,v=np.linalg.svd(Data)
    print('s=',s.shape)
    sum_s=0
    #K = round(2 * shape0 * shape1 / ( r * (shape0 + shape1 + 1)))
    #K = round(1 * m * n / ( (r**0.5) * (m + n + 1)))
    #K = round(2 * m * n / ( (r**0.5) * (m + n + 1)))
    #K = round(1 * m * n / ( (r) * (m + n + 1)))
    K=int(len(s)/r)
    print('K=',K)
    #p=(row*col)/(K*(row+col+1))
    #print('p=',p)
    if K > min(shape0,shape1):
        K = min(shape0,shape1)
    img_c = zeros((shape0,shape1))
    for i in range(K):
        vt=v[i,:].reshape(1,v.shape[1])
        ui=u[:,i].reshape(u.shape[0],1)
        sum_s+=s[i]
        temp=s[i] * ui * vt
        img_c = img_c + temp
        #print('i=',i)
        #print('img_c=',img_c)
    sc=sum_s/sum(s)
    print('score=',sc)

    m=0
    out = np.zeros(im2.shape) 
    Data2=img_c
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
#scipy.misc.imsave('img0.bmp', im2)
im2=im1
row,col=im2.shape # 512,512
size_block0=16
size_block1=16
img_1=pca_image(size_block0,size_block1,row,col,im2,2)
img_2=pca_image(size_block0,size_block1,row,col,im2,8)
img_3=pca_image(size_block0,size_block1,row,col,im2,32)
'''
scipy.misc.imsave('pca_3_im_512_img1.bmp', img_1)
scipy.misc.imsave('pca_3_im_512_img2.bmp', img_2)
scipy.misc.imsave('pca_3_im_512_img3.bmp', img_3)
'''
scipy.misc.imsave('C:/Users/quby/homework/tjhw3/压缩照片对比/pca_3_im_512_img1_16_16.bmp', img_1)
scipy.misc.imsave('C:/Users/quby/homework/tjhw3/压缩照片对比/pca_3_im_512_img2_16_16.bmp', img_2)
scipy.misc.imsave('C:/Users/quby/homework/tjhw3/压缩照片对比/pca_3_im_512_img3_16_16.bmp', img_3)
fig=plt.figure()
fig.suptitle('show picture')

ax=fig.add_subplot(221)
ax.imshow(im2, cmap=cm.gray)
#子图表的标题
ax.set_title('the original image')
ax.axis('off')

ax=fig.add_subplot(222)
ax.imshow(img_1, cmap=cm.gray)
#子图表的标题
ax.set_title('img_1')
ax.axis('off')

ax=fig.add_subplot(223)
ax.imshow(img_2, cmap=cm.gray)
#子图表的标题
ax.set_title('img_2')
ax.axis('off')

ax=fig.add_subplot(224)
ax.imshow(img_3, cmap=cm.gray)
#子图表的标题
ax.set_title('img_3')
ax.axis('off')

plt.show()



