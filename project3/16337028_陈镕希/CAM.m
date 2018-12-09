clc;%清屏

%读取图片
img = imread('原始图片.bmp');

figure(1),subplot(232),imshow(img,[]);title('原始图片');%显示原图片

[M N] = size(img);%记录原图片的尺寸 在这里此图片是512*512

f = double(img);%保存原图片的灰度矩阵 512*512

bs = 16;   %图像块尺寸

p1 = 128;    %保留的维数
p2 = 32;
p3 = 8;

g = im2col(f, [bs bs], 'distinct'); %将图像块分为bs*bs的块，随后每一块重排列生成新矩阵
%以上把图片分成了N个不重叠的16*16的小块，也就是变成了N*256的数据集
%因此这里由512*512变为（16*16）*1024 即256行*1024列 详见https://www.cnblogs.com/rong86/p/3557193.html


% PCA图像压缩
g_m = ones(size(g,1),1)*mean(g);    %计算每块的灰度均值
%ones（创建一个新的矩阵 行数与g相同，即256行，每一行的值都为1）
%mean(g)输出每列的灰度均值，共1024列 两者相乘得到256*1024矩阵，每一列的256个元素都是mean(g)的值

g = g - g_m;%每个灰度减去该列的灰度均值

[E D]=fun_pca(g); %执行pca函数

E_proj1 = E(:,1:p1);   %取最大的p个特征值所对应的特征矢量进行降维
E_proj2 = E(:,1:p2);
E_proj3 = E(:,1:p3);

g_proj1 = g'*E_proj1;  %从bs*bs维映射到p维 1024*256矩阵与256*p矩阵进行相乘，最后得出1024*p矩阵 达到降维目的
g_proj2 = g'*E_proj2;  
g_proj3 = g'*E_proj3;  


% 恢复图像
g_rec1 = g_proj1*E_proj1';%使用1024*p矩阵与256*p矩阵的转置（即p*256矩阵）相乘，得到一个1024*256的矩阵g_rec
g_rec2 = g_proj2*E_proj2';
g_rec3 = g_proj3*E_proj3';

s1 = g_rec1' + g_m;%加处理前每个块的灰度均值
s1 = col2im(s1, [bs bs], [M N], 'distinct');%将图像每一列变为bs*bs的块，随后每一块重排列生成新矩阵
%因此这里由256*1024变为（16*16）*2*512 即512行*512列
s2 = g_rec2' + g_m;
s2 = col2im(s2, [bs bs], [M N], 'distinct');
s3 = g_rec3' + g_m;
s3 = col2im(s3, [bs bs], [M N], 'distinct');

%计算图片信息量 由于var方差函数无法直接计算矩阵方差，因此要先通过std标准差函数计算再平方随后矩阵求和求出所需要的数据
sum(sum((std(s1,0,1).^2)))/sum(sum((std(f,0,1).^2)))
sum(sum((std(s2,0,1).^2)))/sum(sum((std(f,0,1).^2)))
sum(sum((std(s3,0,1).^2)))/sum(sum((std(f,0,1).^2)))

figure(1),subplot(234),imshow(s1,[]);title('压缩为0.5，信息量为0.9980');%生成处理后图片
figure(1),subplot(235),imshow(s2,[]);title('压缩为0.125，信息量为0.9824');
figure(1),subplot(236),imshow(s3,[]);title('压缩为0.015625，信息量为0.9372');

%保存图片
imwrite(s1/255,'s1.bmp');
imwrite(s2/255,'s2.bmp');
imwrite(s3/255,'s3.bmp');



function [E,D] = fun_pca(X)
% do PCA on image patches
% INPUT variables:
% X                  matrix with image patches as columns
% OUTPUT variables:
% E                  特征矢量（第一列对应最大特征值）
% D                  特征值（按下降顺序排列）

covarianceMatrix = X*X'/(size(X,2)-1);%x乘x的转置 除以X矩阵的列-1 即1023 得出协方差矩阵

[E, D] = eig(covarianceMatrix); %返回特征值的对角矩阵 D 和矩阵 E，其列是对应的右特征向量，使得 covarianceMatrix*E = E*D。

[d_out,order] = sort(diag(D),'descend');%diag函数 取对角元素 即矩阵D中特征向量 sort 进行降序排列 与序号一起组成256*2的矩阵

E = E(:,order);%把E的列倒换，即原来第x列变为第257-x列

D = diag(d_out);%把排列好的特征向量再放回到矩阵中去，成为排列好的对角特征向量矩阵D
end