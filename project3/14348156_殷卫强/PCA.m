
%% 利用PCA对图像压缩
 
%% 输入
In = imread('原始图片.bmp');
 
%% 输入参数
num_val = 1;                                 %取前num_val个特征值
size_block = 4;                                       %取size_block*size_block块
 
%% 将原图像矩阵分割成n*n的块，再转化为列矩阵，构成最终矩阵reIn
In = im2double(In);
[row rol] = size(In);
m = 0;
Data = zeros(size_block*size_block,(row/size_block)*(rol/size_block));              % 数据矩阵
for i = 1:size_block:row
    for j = 1:size_block:rol
        m = m+1;
        block = In(i:i+size_block-1,j:j+size_block-1);
        Data(:,m) = block(:);
    end
end
 
%% PCA处理
Data1 = Data - ones(size(Data,1),1)*mean(Data);             % 标准化处理
c = cov(Data1');                                     % 求矩阵协方差矩阵
[vec,val] = eig(c);                                      % 求特征值和特征向量
% 按特征值降序排列
val = diag(val);                                        % 从对角线拿出特征值
[val t] = sort(val,'descend');                             % 特征值降序排列
vec = vec(:,t);                                        % 特征向量也对应改变顺序
 
%% 重构图像
vec_new = vec(:,1:num_val);                                    % 取前k个特征向量
 
    %% 计算所取特征值贡献率
    rata = val./sum(val);
    rata_sum = sum(rata(1:num_val));
    fprintf('选取%g个特征值的贡献率为：%g',num_val,rata_sum);
    
y = vec_new'* Data;                                      % 映射 由公式：y=w'*x
Data2 = vec_new * y;                                    % 重构图像
Data2 = Data2 + ones(size(vec_new, 1), 1) * mean(Data);     % 加均值
m = 0;
for i = 1:size_block:row
    for j = 1:size_block:rol
        m = m + 1;
        block1 = reshape(Data2(:, m), size_block, size_block);        % 列向量块转化为方块
        Out(i:i+size_block-1, j:j+size_block-1) = block1; 
    end
end
 
%% 显示图像
imshow(In),title('原图')
figure,imshow(Out),title('压缩后的图像')
imwrite(Out,'压缩后的图像.jpg')
