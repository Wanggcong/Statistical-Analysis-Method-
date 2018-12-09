[~,txt] = xlsread('\data_selected\000012.csv','A:A');
num = xlsread('\data_selected\000012.csv','B:G'); 

Price=zeros(length(num(:,1)),1);
volume = zeros(length(num(:,1)),1);
for i = 1:length(num(:,1))
    Price(i,1) = (num(i,3)+num(i,4))/2;
    volume(i,1) = num(i,5);
end

R = corrcoef(Price,volume);
rho = corr(volume,Price,'Type','Spearman');

fileID = fopen('question3.txt','w');
fprintf(fileID,'Pearson correlation coefficient: %f\r\n',R(1,2));
fprintf(fileID,'Spearman correlation coefficient: %f\r\n',rho);

% 因此Pearson相关系数为R（1，2）的值[0.0298159151939864]
% Spearman相关系数为[-0.0186959520280351]