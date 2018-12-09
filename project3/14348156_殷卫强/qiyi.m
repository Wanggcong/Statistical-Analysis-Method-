clear all;
close all;
clc;

a=imread('lena.jpg');

imshow(mat2gray(a))
[m n]=size(a);
a=double(a);
r=rank(a);
[s v d]=svd(a);

%re=s*v*d';
re=s(:,:)*v(:,1:1)*d(:,1:1)';
figure;
imshow(mat2gray(re));
imwrite(mat2gray(re),'1.jpg')

re=s(:,:)*v(:,1:20)*d(:,1:20)';
figure;
imshow(mat2gray(re));
imwrite(mat2gray(re),'2.jpg')

re=s(:,:)*v(:,1:80)*d(:,1:80)';
figure;
imshow(mat2gray(re));
imwrite(mat2gray(re),'3.jpg')

re=s(:,:)*v(:,1:150)*d(:,1:150)';
figure;
imshow(mat2gray(re));
imwrite(mat2gray(re),'4.jpg')