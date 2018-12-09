clc
high = table2array(x000012(:,4));
low = table2array(x000012(:,5));
n=size(high,1);
s=(high+low)/2;
v=table2array(x000012(:,6));

r1=corr(s,v,'type','pearson')
r2=corr(s,v,'type','Spearman')
