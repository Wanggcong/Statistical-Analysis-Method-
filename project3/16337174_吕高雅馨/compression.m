close all
clear all
clc

img = imread('ԭʼͼƬ.bmp');
data = im2double(img);
size_block = 16;

featuresToExtract = 128;
[pcaData_2to1, alpha_2to1] = myPCA(data, size_block, featuresToExtract);
featuresToExtract = 32;
[pcaData_8to1, alpha_8to1] = myPCA(data, size_block, featuresToExtract);
featuresToExtract = 8;
[pcaData_32to1, alpha_32to1] = myPCA(data, size_block, featuresToExtract);

%��ʾͼ��
figure
subplot(2,3,2);imshow(img),title('ԭͼ');
subplot(2,3,4);imshow(pcaData_2to1),title(['ѹ����2��1 ��Ϣ�� ', num2str(alpha_2to1)]);
subplot(2,3,5);imshow(pcaData_8to1),title(['ѹ����8��1 ��Ϣ�� ', num2str(alpha_8to1)]);
subplot(2,3,6);imshow(pcaData_32to1),title(['ѹ����32��1 ��Ϣ�� ', num2str(alpha_32to1)]);

