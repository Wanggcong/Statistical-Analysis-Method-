clc
high = table2array(x000001(:,4));
low = table2array(x000001(:,5));
n=size(high,1);
s=(high+low)/2;

%average
average=mean(mean(s));

%mediam
s=sort(s);
mediam=s((n+1)/2);

%0.25
quarter1=s((n-1)/4);

%0.75
quarter3=s(3*(n-1)/4);

%standard
standard=std2(s);

%variance
variance=std2(s)*std2(s);

%variable coefficient
variable_coefficient=standard/average;

%xmax
xmax=max(s)-min(s);

%quarterxmax
quarterxmax=quarter3-quarter1;

%skewness
skewness=n*sum(power(s-average,3))/((n-1)*(n-2)*power(standard,3));

%kurtosis
kurtosis=n*(n+1)*sum(power(s-average,4))/((n-1)*(n-2)*(n-3)*power(standard,4))-3*power(n-1,2)/((n-2)*(n-3));