data =csvread('000006.csv',1,3,[1,3,4341,4]);
average = sum(data,2)/2;
average2 =average;
average(4341,:)=[]; %ɾ��ÿ�չɼ۾����ͷԪ�غ�βԪ��
average2(1,:)=[];
difference = average2 - average; %����õ����ڹɼ۲�
subplot(1,2,1),Histogram = histogram(difference);  %ֱ��ͼ
title('06���ڹɼ۲�ֱֵ��ͼ','fontsize',16);
subplot(1,2,2),qqplot(difference);  %QQͼ