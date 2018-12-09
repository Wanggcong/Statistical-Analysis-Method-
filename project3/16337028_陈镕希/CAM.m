clc;%����

%��ȡͼƬ
img = imread('ԭʼͼƬ.bmp');

figure(1),subplot(232),imshow(img,[]);title('ԭʼͼƬ');%��ʾԭͼƬ

[M N] = size(img);%��¼ԭͼƬ�ĳߴ� �������ͼƬ��512*512

f = double(img);%����ԭͼƬ�ĻҶȾ��� 512*512

bs = 16;   %ͼ���ߴ�

p1 = 128;    %������ά��
p2 = 32;
p3 = 8;

g = im2col(f, [bs bs], 'distinct'); %��ͼ����Ϊbs*bs�Ŀ飬���ÿһ�������������¾���
%���ϰ�ͼƬ�ֳ���N�����ص���16*16��С�飬Ҳ���Ǳ����N*256�����ݼ�
%���������512*512��Ϊ��16*16��*1024 ��256��*1024�� ���https://www.cnblogs.com/rong86/p/3557193.html


% PCAͼ��ѹ��
g_m = ones(size(g,1),1)*mean(g);    %����ÿ��ĻҶȾ�ֵ
%ones������һ���µľ��� ������g��ͬ����256�У�ÿһ�е�ֵ��Ϊ1��
%mean(g)���ÿ�еĻҶȾ�ֵ����1024�� ������˵õ�256*1024����ÿһ�е�256��Ԫ�ض���mean(g)��ֵ

g = g - g_m;%ÿ���Ҷȼ�ȥ���еĻҶȾ�ֵ

[E D]=fun_pca(g); %ִ��pca����

E_proj1 = E(:,1:p1);   %ȡ����p������ֵ����Ӧ������ʸ�����н�ά
E_proj2 = E(:,1:p2);
E_proj3 = E(:,1:p3);

g_proj1 = g'*E_proj1;  %��bs*bsάӳ�䵽pά 1024*256������256*p���������ˣ����ó�1024*p���� �ﵽ��άĿ��
g_proj2 = g'*E_proj2;  
g_proj3 = g'*E_proj3;  


% �ָ�ͼ��
g_rec1 = g_proj1*E_proj1';%ʹ��1024*p������256*p�����ת�ã���p*256������ˣ��õ�һ��1024*256�ľ���g_rec
g_rec2 = g_proj2*E_proj2';
g_rec3 = g_proj3*E_proj3';

s1 = g_rec1' + g_m;%�Ӵ���ǰÿ����ĻҶȾ�ֵ
s1 = col2im(s1, [bs bs], [M N], 'distinct');%��ͼ��ÿһ�б�Ϊbs*bs�Ŀ飬���ÿһ�������������¾���
%���������256*1024��Ϊ��16*16��*2*512 ��512��*512��
s2 = g_rec2' + g_m;
s2 = col2im(s2, [bs bs], [M N], 'distinct');
s3 = g_rec3' + g_m;
s3 = col2im(s3, [bs bs], [M N], 'distinct');

%����ͼƬ��Ϣ�� ����var������޷�ֱ�Ӽ�����󷽲���Ҫ��ͨ��std��׼���������ƽ������������������Ҫ������
sum(sum((std(s1,0,1).^2)))/sum(sum((std(f,0,1).^2)))
sum(sum((std(s2,0,1).^2)))/sum(sum((std(f,0,1).^2)))
sum(sum((std(s3,0,1).^2)))/sum(sum((std(f,0,1).^2)))

figure(1),subplot(234),imshow(s1,[]);title('ѹ��Ϊ0.5����Ϣ��Ϊ0.9980');%���ɴ����ͼƬ
figure(1),subplot(235),imshow(s2,[]);title('ѹ��Ϊ0.125����Ϣ��Ϊ0.9824');
figure(1),subplot(236),imshow(s3,[]);title('ѹ��Ϊ0.015625����Ϣ��Ϊ0.9372');

%����ͼƬ
imwrite(s1/255,'s1.bmp');
imwrite(s2/255,'s2.bmp');
imwrite(s3/255,'s3.bmp');



function [E,D] = fun_pca(X)
% do PCA on image patches
% INPUT variables:
% X                  matrix with image patches as columns
% OUTPUT variables:
% E                  ����ʸ������һ�ж�Ӧ�������ֵ��
% D                  ����ֵ�����½�˳�����У�

covarianceMatrix = X*X'/(size(X,2)-1);%x��x��ת�� ����X�������-1 ��1023 �ó�Э�������

[E, D] = eig(covarianceMatrix); %��������ֵ�ĶԽǾ��� D �;��� E�������Ƕ�Ӧ��������������ʹ�� covarianceMatrix*E = E*D��

[d_out,order] = sort(diag(D),'descend');%diag���� ȡ�Խ�Ԫ�� ������D���������� sort ���н������� �����һ�����256*2�ľ���

E = E(:,order);%��E���е�������ԭ����x�б�Ϊ��257-x��

D = diag(d_out);%�����кõ����������ٷŻص�������ȥ����Ϊ���кõĶԽ�������������D
end