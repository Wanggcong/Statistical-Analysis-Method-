x=csvread('cha6.csv');
%k=histogram(x);
[a,b]=hist(x);
bar(b,a/sum(a));            %Ö±·½Í¼
h=qqplot(x);                %ÕýÌ¬QQÍ¼
set(h(3),'linestyle','-','linewidth',2);