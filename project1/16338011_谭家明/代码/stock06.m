function ST6 = stock06()
data =csvread('000006.csv',1,3,[1,3,4341,4]);
average = sum(data,2)/2;  %ÿ�չɼ�
subplot(1,2,1),h1=histogram(average,[3:1:39]);  %ֱ��ͼ
h1.Normalization = 'probability';
title('06�ɼ�Ƶ��ֱ��ͼ','fontsize',16);
subplot(1,2,2),qqplot(average);  %QQͼ

