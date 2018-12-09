M = readtable('000001.csv');
N = readtable('000006.csv');

date1 = M.date;
date6 = N.date;

daily1 = (M.high+M.low)/2;
daily6 = (N.high+N.low)/2;

[same_date,ia,ib] = intersect(date1,date6);

same_daily = zeros(length(same_date), 2);
same_daily(:,1) = daily1(ia);
same_daily(:,2) = daily6(ib);

pearson_corr = corr(same_daily(:,1),same_daily(:,2),'type','pearson');
spearman_corr = corr(same_daily(:,1),same_daily(:,2),'type','spearman');



list = dir(['C:\Users\myz\Desktop\data_selected\', '*.csv']);
len = length(list);
total = cell(100,1);
for n = 1:len
   file_name = strcat('C:\Users\myz\Desktop\data_selected\', list(n).name);
   total{n} = file_name;
end

pearson_matrix = zeros(100,100);
spearman_matrix = zeros(100,100);

for i = 1:99
    for j = i+1:100
        [corr1,corr2] = calculate_corr(total{i}, total{j});
        pearson_matrix(i,j) = corr1;
        spearman_matrix(i,j) = corr2;
    end
end







