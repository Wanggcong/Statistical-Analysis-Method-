
%% ����PCA��ͼ��ѹ��
 
%% ����
In = imread('ԭʼͼƬ.bmp');
 
%% �������
num_val = 1;                                 %ȡǰnum_val������ֵ
size_block = 4;                                       %ȡsize_block*size_block��
 
%% ��ԭͼ�����ָ��n*n�Ŀ飬��ת��Ϊ�о��󣬹������վ���reIn
In = im2double(In);
[row rol] = size(In);
m = 0;
Data = zeros(size_block*size_block,(row/size_block)*(rol/size_block));              % ���ݾ���
for i = 1:size_block:row
    for j = 1:size_block:rol
        m = m+1;
        block = In(i:i+size_block-1,j:j+size_block-1);
        Data(:,m) = block(:);
    end
end
 
%% PCA����
Data1 = Data - ones(size(Data,1),1)*mean(Data);             % ��׼������
c = cov(Data1');                                     % �����Э�������
[vec,val] = eig(c);                                      % ������ֵ����������
% ������ֵ��������
val = diag(val);                                        % �ӶԽ����ó�����ֵ
[val t] = sort(val,'descend');                             % ����ֵ��������
vec = vec(:,t);                                        % ��������Ҳ��Ӧ�ı�˳��
 
%% �ع�ͼ��
vec_new = vec(:,1:num_val);                                    % ȡǰk����������
 
    %% ������ȡ����ֵ������
    rata = val./sum(val);
    rata_sum = sum(rata(1:num_val));
    fprintf('ѡȡ%g������ֵ�Ĺ�����Ϊ��%g',num_val,rata_sum);
    
y = vec_new'* Data;                                      % ӳ�� �ɹ�ʽ��y=w'*x
Data2 = vec_new * y;                                    % �ع�ͼ��
Data2 = Data2 + ones(size(vec_new, 1), 1) * mean(Data);     % �Ӿ�ֵ
m = 0;
for i = 1:size_block:row
    for j = 1:size_block:rol
        m = m + 1;
        block1 = reshape(Data2(:, m), size_block, size_block);        % ��������ת��Ϊ����
        Out(i:i+size_block-1, j:j+size_block-1) = block1; 
    end
end
 
%% ��ʾͼ��
imshow(In),title('ԭͼ')
figure,imshow(Out),title('ѹ�����ͼ��')
imwrite(Out,'ѹ�����ͼ��.jpg')
