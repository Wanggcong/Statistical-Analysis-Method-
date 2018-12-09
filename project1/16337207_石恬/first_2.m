clc
high = table2array(x000006(:,4));
low = table2array(x000006(:,5));
n=size(high,1);
s=(high+low)/2;

%直方图
[counts,centers] = hist(s, 100);
figure
bar(centers, counts / sum(counts))
title('直方图1');

%QQ图
figure
qqplot(s);

div=s(2:n)-s(1:n-1);
%差值直方图
[counts,centers] = hist(div, 100);
figure
bar(centers, counts / sum(counts))
title('差值直方图');

%差值QQ图
figure
qqplot(div);