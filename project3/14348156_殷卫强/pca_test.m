function pca_test
clear;close all;

img=imread('lena.bmp');           
figure(1),subplot(121),imshow(img,[]);title('Original Image');
[M N] = size(img);
f = double(img);
bs = 16;   %ͼ���ߴ�
p = 30;    %������ά��

% PCAͼ��ѹ��
g = im2col(f, [bs bs], 'distinct'); %��ͼ���ת������ʸ����ʾ
g_m = ones(size(g,1),1)*mean(g);    %����ÿ����ĻҶȾ�ֵ
g = g - g_m;
[E D]=fun_pca(g);
E_proj = E(:,1:p);   %ȡ����p������ֵ����Ӧ������ʸ�����н�ά
g_proj = g'*E_proj;  %��bs*bsάӳ�䵽pά

% �ָ�ͼ��
g_rec = g_proj*E_proj';
s = g_rec' + g_m;
s = col2im(s, [bs bs], [M N], 'distinct');
figure(1),subplot(122),imshow(s,[]);title('Recovered Image');

function [E,D] = fun_pca(X)
% do PCA on image patches
% INPUT variables:
% X                  matrix with image patches as columns
% OUTPUT variables:
% E                  ����ʸ������һ�ж�Ӧ�������ֵ��
% D                  ����ֵ�����½�˳�����У�
% Calculate the eigenvalues and eigenvectors
covarianceMatrix = X*X'/(size(X,2)-1);
[E, D] = eig(covarianceMatrix);
% Sort the eigenvalues and recompute matrices
[d_out,order] = sort(diag(D),'descend');
E = E(:,order);
d = diag(D); 
D = diag(d(order));
