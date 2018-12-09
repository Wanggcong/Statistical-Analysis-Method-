function pca(P)
% PΪѹ����

img = imread('ԭʼͼƬ.bmp');
figure(1),subplot(131),imshow(img,[]);
title('Original Image');
[M N] = size(img);
block_size = 16;    %�ӿ�ĳߴ�
orignal_W = block_size * block_size;  %��ʼά��
end_W = P * orignal_W;  %ѹ�����ά��

% PCA
colMat = im2col(double(img), [block_size block_size], 'distinct');    %��ͼ���תΪ������
mean_ = ones(size(colMat,1),1) * mean(colMat);   %����ÿ��ĻҶȾ�ֵ
colMat = colMat - mean_; %�׻�

covarianceMat = colMat * colMat' / (size(colMat,2) - 1);    %����������
[E,D] = eig(covarianceMat); %EΪ����������DΪ����ֵ
[temp,order] = sort(diag(D),'descend');
E = E(:,order); %������ֵ��������
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

