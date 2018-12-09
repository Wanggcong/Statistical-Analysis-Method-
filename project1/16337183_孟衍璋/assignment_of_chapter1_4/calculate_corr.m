function [corr1, corr2] = calculate_corr(file1, file2)
    M = readtable(file1);
    N = readtable(file2);

    date1 = M.date;
    date6 = N.date;

    daily1 = (M.high+M.low)/2;
    daily6 = (N.high+N.low)/2;

    [same_date,ia,ib] = intersect(date1,date6);

    same_daily = zeros(length(same_date), 2);
    same_daily(:,1) = daily1(ia);
    same_daily(:,2) = daily6(ib);

    corr1 = corr(same_daily(:,1),same_daily(:,2),'type','pearson');
    corr2 = corr(same_daily(:,1),same_daily(:,2),'type','spearman');
end