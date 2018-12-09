import numpy as np
from PIL import Image
from PIL import ImageChops
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

# split img to N*256 blocks
# get Image object
# return ndarray object
def splitImage(im):
    im = im.convert('L')
    width,height = im.size
    im_list = []
    for i in range(height//16):
        for j in range(width//16):
            box = np.array(im.crop((j*16,i*16,j*16+16,i*16+16)))
            sample = box.reshape(1,256)
            im_list.extend((sample))
    return np.array(im_list)

# recover img to N*256 blocks
# get ndarray object
# return Image object
def combineImage(img):
    x = 0
    width = 512
    height = 512
    img_new = Image.new('L',(width,height))
    for i in range(width//16):
        for j in range(height//16):
            block =  img[x].reshape(16,16)
            sample = Image.fromarray(block).convert('L')
            img_new.paste(sample,(j*16,i*16,j*16+16,i*16+16))
            x += 1
    return img_new

# PCA operations
def pca(img,n):
    # compression, to n dimensions 
    pca = PCA(n_components=n, copy=True, whiten=False)
    compression = pca.fit_transform(img)
    # info rate
    contri = 0
    for x in pca.explained_variance_ratio_:
        contri += x    
    # reconstruction
    recon_arr = pca.inverse_transform(compression)
    recon = combineImage(recon_arr)    
    return compression,contri,recon

# calculate different
def dif(im,recon):
    diff = ImageChops.difference(im,recon)
    return diff

# print imgs
def showim(im,cmpr,recon,diff,contri,n):     
    plt.figure()
    ax = plt.subplot(232)
    plt.imshow(im)
    ax.set_title('origin')

    ax = plt.subplot(223)
    plt.imshow(recon)
    ax.set_title('cmpr:{}, info:{:.5f}'.format(256//n,contri))
    
    ax = plt.subplot(224)
    plt.imshow(diff)
    ax.set_title('diff')
    
    plt.show()

# process of a image
def process(im,n):
    img = splitImage(im)
    cmpr,contri,recon = pca(img,n)
    diff = dif(im,recon)
    showim(im,cmpr,recon,diff,contri,n)
    
def main(): 
    im = Image.open('img/origin.bmp')
    process(im,128)
    process(im,32)
    process(im,8)

if __name__ == '__main__':
    main()
    