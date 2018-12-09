function [r1,r2]=first_4(A,B)
high1=[];
high2=[];
low1=[];
low2=[];
time1=table2array(A(:,1));
time2=table2array(B(:,1));
ohigh1=table2array(A(:,4));
ohigh2=table2array(B(:,4));
olow1=table2array(A(:,5));
olow2=table2array(B(:,5));
[C,IA,IB] = intersect(time1,time2);

for i=1:size(IA,1)
    high1(i)=ohigh1(IA(i));
    high2(i)=ohigh2(IB(i));
    low1(i)=olow1(IA(i));
    low2(i)=olow2(IB(i));
end
high1=high1';
high2=high2';
low1=low1';
low2=low2';
s1=(high1+low1)/2;
s2=(high2+low2)/2;
r1=corr(s1,s2,'type','pearson');
r2=corr(s1,s2,'type','Spearman');