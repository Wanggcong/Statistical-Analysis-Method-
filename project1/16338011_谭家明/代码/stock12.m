data =csvread('000012.csv',1,3,[1,3,4428,4]);
average = sum(data,2)/2; %每日股价
trade = csvread('000012.csv',1,5,[1,5,4428,5]);  %每日成交量
r1=corr(average,trade,'type','pearson');
r2=corr(average,trade,'type','Spearman');
fprintf('pearson相关系数：%g\nSpearman相关系数：%g',r1,r2);