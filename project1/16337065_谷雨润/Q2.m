x=csvread('average6.csv');
[a,b]=hist(x);
bar(b,a/sum(a));            %Ö±·½Í¼
h=qqplot(data);             %ÕıÌ¬QQÍ¼
set(h(3),'linestyle','-','linewidth',2);