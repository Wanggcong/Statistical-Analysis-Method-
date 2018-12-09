function [R1,P1] = calculate_pearson(file1, file2)
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

    [R1,P1] = corrcoef(same_daily(:,1),same_daily(:,2));
end