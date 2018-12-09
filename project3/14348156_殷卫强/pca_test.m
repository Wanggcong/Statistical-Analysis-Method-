function pca_test
clear;close all;

img=imread('lena.bmp');           
figure(1),subplot(121),imshow(img,[]);title('Original Image');
[M N] = size(img);
f = double(img);
bs = 16;   %图像块尺寸
p = 30;    %保留的维数

% PCA图像压缩
g = im2col(f, [bs bs], 'distinct'); %将图像块转换成列矢量表示
g_m = ones(size(g,1),1)*mean(g);    %计算每个块的灰度均值
g = g - g_m;
[E D]=fun_pca(g);
E_proj = E(:,1:p);   %取最大的p个特征值所对应的特征矢量进行降维
g_proj = g'*E_proj;  %从bs*bs维映射到p维

% 恢复图像
g_rec = g_proj*E_proj';
s = g_rec' + g_m;
s = col2im(s, [bs bs], [M N], 'distinct');
figure(1),subplot(122),imshow(s,[]);title('Recovered Image');

function [E,D] = fun_pca(X)
% do PCA on image patches
% INPUT variables:
% X                  matrix with image patches as columns
% OUTPUT variables:
% E                  特征矢量（第一列对应最大特征值）
% D                  特征值（按下降顺序排列）
% Calculate the eigenvalues and eigenvectors
covarianceMatrix = X*X'/(size(X,2)-1);
[E, D] = eig(covarianceMatrix);
% Sort the eigenvalues and recompute matrices
[d_out,order] = sort(diag(D),'descend');
E = E(:,order);
d = diag(D); 
D = diag(d(order));
