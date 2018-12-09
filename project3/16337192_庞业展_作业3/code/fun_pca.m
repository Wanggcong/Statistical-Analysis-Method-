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