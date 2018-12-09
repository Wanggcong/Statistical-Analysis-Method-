data =csvread('000006.csv',1,3,[1,3,4341,4]);
average = sum(data,2)/2;
average2 =average;
average(4341,:)=[]; %删除每日股价矩阵的头元素和尾元素
average2(1,:)=[];
difference = average2 - average; %相减得到相邻股价差
subplot(1,2,1),Histogram = histogram(difference);  %直方图
title('06相邻股价差值直方图','fontsize',16);
subplot(1,2,2),qqplot(difference);  %QQ图