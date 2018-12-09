x=csvread('ave12.csv');
y=csvread('volume12.csv');
c1=corr(x,y,'type','pearson')
c2=corr(x,y,'type','spearman')