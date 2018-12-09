function[pcaData, alpha] = myPCA(data, size_block, featuresToExtract);
%����: data,ԭʼͼ�������
%      size_block����ԭʼͼ���з�Ϊ������С�飬С��ı߳�
%      featuresToExtract,��ȡ�����ɷ���
%���: pcaData,ѹ����ͼ�������
%      alpha,��ȡ�����ɷ��ۼƷ�����ʣ�������ʾѹ�������Ϣ���ٷֱ�


    %�ó�ԭʼͼ�����ݵĳߴ�
    [row col] = size(data);
    slice_size = size_block * size_block;      %�и��Сͼ����ά��
    m = 0;
    matrix = zeros(slice_size, (row*col)/slice_size);      %256*1024����
    for i = 1:size_block:row
        for j = 1:size_block:col
            m = m+1;
            block = data(i:i+size_block-1, j:j+size_block-1);
            matrix(:,m) = block(:);
        end
    end
    
    %��׼������
    normalizedData = matrix - ones(size(matrix,1),1)*mean(matrix);
    
    %����ؾ��󣨱�׼�����Э�������
    covarianceMatrix = cov(normalizedData');
    
    %������ֵ����������
    [eigVec, eigVal] = eig(covarianceMatrix);
    eigVal = diag(eigVal);
    [eigVal t] = sort(eigVal, 'descend');
    eigVec = eigVec(:,t);
    
    
    projectionVectors = eigVec(:,1:featuresToExtract);
    %������ȡ����ֵ������(��Ϣ����С��
    alpha = sum(eigVal(1:featuresToExtract))/sum(eigVal);
    
    %�ع�ͼ��
    y = projectionVectors'* matrix;
    pcaData = projectionVectors * y + ones(size(projectionVectors,1),1)*mean(matrix);
    m= 0;
    for i = 1:size_block:row
        for j = 1:size_block:col
            m = m + 1;
            block1 = reshape(pcaData(:,m), size_block, size_block);        % ��������ת��Ϊ����
            Out(i:i+size_block-1, j:j+size_block-1) = block1; 
        end
    end
    pcaData = Out;
end
    
    
    