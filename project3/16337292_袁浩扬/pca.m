function pca(P)
% P为压缩率

img = imread('原始图片.bmp');
figure(1),subplot(131),imshow(img,[]);
title('Original Image');
[M N] = size(img);
block_size = 16;    %子块的尺寸
orignal_W = block_size * block_size;  %初始维度
end_W = P * orignal_W;  %压缩后的维度

% PCA
colMat = im2col(double(img), [block_size block_size], 'distinct');    %将图像块转为列向量
mean_ = ones(size(colMat,1),1) * mean(colMat);   %计算每块的灰度均值
colMat = colMat - mean_; %白化

covarianceMat = colMat * colMat' / (size(colMat,2) - 1);    %计算伴随矩阵
[E,D] = eig(covarianceMat); %E为特征向量，D为特征值
[temp,order] = sort(diag(D),'descend');
E = E(:,order); %按特征值降序排列
E_leave = E(:,1:end_W);
g_proj = colMat' * E_leave;
g_rec = g_proj * E_leave';
s = g_rec' + mean_;
s = col2im(s, [block_size block_size], [M N], 'distinct');
figure(1),subplot(132),imshow(s,[]);
title('Recovered img');

sub = double(img) - s;
figure(1),subplot(133),imshow(sub,[]);
title('sub img');

end

