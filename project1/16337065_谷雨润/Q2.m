x=csvread('average6.csv');
[a,b]=hist(x);
bar(b,a/sum(a));            %ֱ��ͼ
h=qqplot(data);             %��̬QQͼ
set(h(3),'linestyle','-','linewidth',2);