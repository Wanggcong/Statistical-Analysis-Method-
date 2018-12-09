function pca_test(P)                %PΪ������ά��
img=imread('Lena.bmp');           
figure(1),subplot(121),imshow(img,[]);title('Original Image');
[M, N] = size(img);
f = double(img);
bs = 16;                            %ͼ���ߴ�
% PCAͼ��ѹ��
g = im2col(f, [bs bs], 'distinct'); %��ͼ���ת������ʸ����ʾ
g_m = ones(size(g,1),1)*mean(g);    %����ÿ����ĻҶȾ�ֵ
g = g - g_m;                        %�������ֵ��
[E, D]=fun_pca(g);                  % EΪ����ʸ������һ�ж�Ӧ�������ֵ��
                                    % DΪ����ֵ�����½�˳�����У�
E_proj = E(:,1:P);                  %ȡ����p������ֵ����Ӧ������ʸ�����н�ά
g_proj = g'*E_proj;                 %��bs*bsάӳ�䵽pά

% �ָ�ͼ��
g_rec = g_proj*E_proj';
s = g_rec' + g_m;
s = col2im(s, [bs bs], [M N], 'distinct');
figure(1),subplot(122),imshow(s,[]);title('Recovered Image');
  