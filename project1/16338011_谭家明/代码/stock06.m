function ST6 = stock06()
data =csvread('000006.csv',1,3,[1,3,4341,4]);
average = sum(data,2)/2;  %每日股价
subplot(1,2,1),h1=histogram(average,[3:1:39]);  %直方图
h1.Normalization = 'probability';
title('06股价频率直方图','fontsize',16);
subplot(1,2,2),qqplot(average);  %QQ图

