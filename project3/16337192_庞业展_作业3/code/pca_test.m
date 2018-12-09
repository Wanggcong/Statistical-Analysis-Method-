function pca_test(P)                %P为保留的维数
img=imread('Lena.bmp');           
figure(1),subplot(121),imshow(img,[]);title('Original Image');
[M, N] = size(img);
f = double(img);
bs = 16;                            %图像块尺寸
% PCA图像压缩
g = im2col(f, [bs bs], 'distinct'); %将图像块转换成列矢量表示
g_m = ones(size(g,1),1)*mean(g);    %计算每个块的灰度均值
g = g - g_m;                        %进行零均值化
[E, D]=fun_pca(g);                  % E为特征矢量（第一列对应最大特征值）
                                    % D为特征值（按下降顺序排列）
E_proj = E(:,1:P);                  %取最大的p个特征值所对应的特征矢量进行降维
g_proj = g'*E_proj;                 %从bs*bs维映射到p维

% 恢复图像
g_rec = g_proj*E_proj';
s = g_rec' + g_m;
s = col2im(s, [bs bs], [M N], 'distinct');
figure(1),subplot(122),imshow(s,[]);title('Recovered Image');
  