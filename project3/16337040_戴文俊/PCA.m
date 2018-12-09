img=imread('lena.bmp');           
[M, N] = size(img);
f = double(img);
bs = 16;   %block size
p = 128;    %remaining dimension

% PCA
x = im2col(f, [bs bs], 'distinct'); %xet 1024 blocks
x_m = ones(size(x,1),1)*mean(x);    %calculate the mean of each block
x = x - x_m;                        %x_i - x_mean

cov = x*x'/(size(x,2)-1);
[E, D] = eig(cov);
size(E)
[~,order] = sort(diag(D),'descend');
E = E(:,order);
d = diag(D); 
D = diag(d(order));
%calculate the contribution rate
info = sum(d(256-p:256))/sum(d)
E_proj = E(:,1:p);   %find p_max eigenvectors
x_proj = x'*E_proj;  %map dim(bs*bs) to p dimension

% recover the image
x_rec = x_proj*E_proj'; 
s = x_rec' + x_m;
s = col2im(s, [bs bs], [M N], 'distinct');

subplot(121),imshow(img,[]);title('Original Image');
subplot(122),imshow(s,[]);title(['r = ',num2str(p/256)]);

