data =csvread('000012.csv',1,3,[1,3,4428,4]);
average = sum(data,2)/2; %ÿ�չɼ�
trade = csvread('000012.csv',1,5,[1,5,4428,5]);  %ÿ�ճɽ���
r1=corr(average,trade,'type','pearson');
r2=corr(average,trade,'type','Spearman');
fprintf('pearson���ϵ����%g\nSpearman���ϵ����%g',r1,r2);