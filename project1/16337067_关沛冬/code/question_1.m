[~,txt] = xlsread('\data_selected\000001.csv','A:A');
num = xlsread('\data_selected\000001.csv','B:G'); 

sum(num(:,1));

Price=zeros(length(num(:,1)),1);
for i = 1:length(num(:,1))
    Price(i,1) = (num(i,3)+num(i,4))/2;
end

Average = mean(Price);
Median = median(Price);
Max = max(Price);
Minimum = min(Price);
Q1 = prctile(Price,25);
Q3 = prctile(Price,75);
Variance = var(Price);
Standard_deviation = std(Price);
CV = (Standard_deviation / Average)* 100;
Range = Max - Minimum;
R1 = Q3-Q1;
g1 = skewness(Price);
n = length(Price);
g2 = n*(n+1)/((n-1)*(n-2)*(n-3))/(Standard_deviation^4)*(sum((Price-Average).^4))-3*((n-1)^2)/((n-2)*(n-3));

fileID = fopen('question1.txt','w');
fprintf(fileID,'Average: %f\r\n',Average);
fprintf(fileID,'Median: %f\r\n',Median);
fprintf(fileID,'0.25 Quantile: %f\r\n',Q1);
fprintf(fileID,'0.75 Quantile: %f\r\n',Q3);
fprintf(fileID,'Variance: %f\r\n',Variance);
fprintf(fileID,'Standard deviation: %f\r\n',Standard_deviation);
fprintf(fileID,'Coefficient of variation: %f\r\n',CV);
fprintf(fileID,'Range: %f\r\n',Range);
fprintf(fileID,'Four fraction range: %f\r\n',R1);
fprintf(fileID,'Skewness: %f\r\n',g1);
fprintf(fileID,'Kurtosis: %f\r\n',g2);
fclose(fileID);

