function[pcaData, alpha] = myPCA(data, size_block, featuresToExtract);
%输入: data,原始图像的数据
%      size_block，将原始图像切分为正方形小块，小块的边长
%      featuresToExtract,提取的主成分数
%输出: pcaData,压缩后图像的数据
%      alpha,提取的主成分累计方差贡献率，用来表示压缩后的信息量百分比


    %得出原始图像数据的尺寸
    [row col] = size(data);
    slice_size = size_block * size_block;      %切割成小图像块的维数
    m = 0;
    matrix = zeros(slice_size, (row*col)/slice_size);      %256*1024矩阵
    for i = 1:size_block:row
        for j = 1:size_block:col
            m = m+1;
            block = data(i:i+size_block-1, j:j+size_block-1);
            matrix(:,m) = block(:);
        end
    end
    
    %标准化处理
    normalizedData = matrix - ones(size(matrix,1),1)*mean(matrix);
    
    %求相关矩阵（标准化后的协方差矩阵）
    covarianceMatrix = cov(normalizedData');
    
    %求特征值和特征向量
    [eigVec, eigVal] = eig(covarianceMatrix);
    eigVal = diag(eigVal);
    [eigVal t] = sort(eigVal, 'descend');
    eigVec = eigVec(:,t);
    
    
    projectionVectors = eigVec(:,1:featuresToExtract);
    %计算所取特征值贡献率(信息量大小）
    alpha = sum(eigVal(1:featuresToExtract))/sum(eigVal);
    
    %重构图像
    y = projectionVectors'* matrix;
    pcaData = projectionVectors * y + ones(size(projectionVectors,1),1)*mean(matrix);
    m= 0;
    for i = 1:size_block:row
        for j = 1:size_block:col
            m = m + 1;
            block1 = reshape(pcaData(:,m), size_block, size_block);        % 列向量块转化为方块
            Out(i:i+size_block-1, j:j+size_block-1) = block1; 
        end
    end
    pcaData = Out;
end
    
    
    