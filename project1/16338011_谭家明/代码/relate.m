%function M = relate() %求出相关性最强和最弱的股票
pear = importdata('pearson系数.csv'); %读取文件数据
spear = importdata('Spearman系数.csv');
Pear1 = abs(pear); %取绝对值
Pear2 = abs(pear);
Spear1 = abs(spear);
Spear2 = abs(spear);
index1 = 0;
index2 = 0;
fprintf('根据pearson矩阵得知\n相关性最强的五对股票位置所在是：\n');
[r1,c1] = size(Pear1);
for i = 1:r1
    for j = 1:c1
        if i == j || i > j
            Pear1(i,j) = 0;  %把重复的置位0
        end
    end
end
    
for i = 1:5
    [index1,index2] = find(Pear1==max(max(Pear1))); %寻找出矩阵中最大元素的位置
    Pear1(index1,index2) = 0; %将其置0，以便寻找下一轮最大的元素
    fprintf('%g  %g\n',index1,index2);
    index1=0;
    index2=0;
end

[r2,c2] = size(Pear2);
for i = 1:r2
    for j = 1:c2
        if i == j || i > j
            Pear2(i,j) = 1;  %将矩阵下三角置1
        end
    end
end
fprintf('相关性最弱的五对股票位置所在是：\n');
for i = 1:5
    [index1,index2] = find(Pear2==min(min(Pear2)));%寻找出矩阵中最小元素的位置
    Pear2(index1,index2) = 1;%将其置1，以便寻找下一轮最小的元素
    fprintf('%g  %g\n',index1,index2);
    index1=0;
    index2=0;
end
fprintf('根据spearman矩阵得知\n相关性最强的五对股票位置所在是：\n');
[r1,c1] = size(Spear1);
for i = 1:r1
    for j = 1:c1
        if i == j || i > j
            Spear1(i,j) = 0;
        end
    end
end
    
for i = 1:5
    [index1,index2] = find(Spear1==max(max(Spear1)));
    Spear1(index1,index2) = 0;
    fprintf('%g  %g\n',index1,index2);
    index1=0;
    index2=0;
end

[r2,c2] = size(Spear2);
for i = 1:r2
    for j = 1:c2
        if i == j || i > j
            Spear2(i,j) = 1;
        end
    end
end
fprintf('相关性最弱的五对股票位置所在是：\n');
for i = 1:5
    [index1,index2] = find(Spear2==min(min(Spear2)));
    Spear2(index1,index2) = 1;
    fprintf('%g  %g\n',index1,index2);
    index1=0;
    index2=0;
end
