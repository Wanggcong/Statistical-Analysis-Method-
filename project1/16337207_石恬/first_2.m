clc
high = table2array(x000006(:,4));
low = table2array(x000006(:,5));
n=size(high,1);
s=(high+low)/2;

%ֱ��ͼ
[counts,centers] = hist(s, 100);
figure
bar(centers, counts / sum(counts))
title('ֱ��ͼ1');

%QQͼ
figure
qqplot(s);

div=s(2:n)-s(1:n-1);
%��ֱֵ��ͼ
[counts,centers] = hist(div, 100);
figure
bar(centers, counts / sum(counts))
title('��ֱֵ��ͼ');

%��ֵQQͼ
figure
qqplot(div);