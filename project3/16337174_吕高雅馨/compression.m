close all
clear all
clc

img = imread('原始图片.bmp');
data = im2double(img);
size_block = 16;

featuresToExtract = 128;
[pcaData_2to1, alpha_2to1] = myPCA(data, size_block, featuresToExtract);
featuresToExtract = 32;
[pcaData_8to1, alpha_8to1] = myPCA(data, size_block, featuresToExtract);
featuresToExtract = 8;
[pcaData_32to1, alpha_32to1] = myPCA(data, size_block, featuresToExtract);

%显示图像
figure
subplot(2,3,2);imshow(img),title('原图');
subplot(2,3,4);imshow(pcaData_2to1),title(['压缩率2：1 信息量 ', num2str(alpha_2to1)]);
subplot(2,3,5);imshow(pcaData_8to1),title(['压缩率8：1 信息量 ', num2str(alpha_8to1)]);
subplot(2,3,6);imshow(pcaData_32to1),title(['压缩率32：1 信息量 ', num2str(alpha_32to1)]);

