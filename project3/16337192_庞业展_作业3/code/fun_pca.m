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