x=csvread('cha6.csv');
%k=histogram(x);
[a,b]=hist(x);
bar(b,a/sum(a));            %ֱ��ͼ
h=qqplot(x);                %��̬QQͼ
set(h(3),'linestyle','-','linewidth',2);