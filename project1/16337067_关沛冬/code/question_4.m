cd data_selected;
T = readtable('000001.csv');
    txt1 = table2array(T(:,1));t1 = table2array(T(:,4)); t2 = table2array(T(:,5)); 
    num1 = (t1(:,1)+t2(:,1))/2; 
T = readtable('000006.csv');
    txt2 = table2array(T(:,1));t1 = table2array(T(:,4)); t2 = table2array(T(:,5)); 
    num2 = (t1(:,1)+t2(:,1))/2; 
cd ..;
SameDate = intersect(txt1,txt2);
[price1,price2] = GetData(txt1,txt2,num1,num2);

R_Pearson = corrcoef(price1,price2);
R_Spearman = corr(price1,price2,'Type','Spearman');

fileID = fopen('question4.txt','w');
fprintf(fileID,'Pearson correlation coefficient: %f\r\n',R_Pearson(1,2));
fprintf(fileID,'Spearman correlation coefficient: %f\r\n',R_Spearman);
%由此可见，1股票和6股票的Pearson相关系数为[0.777338482893102]
% Spearman相关系数为[0.510193887950088]

cd data_selected;
List = ls;
cd .. ;
my_dir = '\data_selected\';

R_Pearson_Table = zeros(length(List)-2,length(List)-2);
R_Spearman_Table = zeros(length(List)-2,length(List)-2);

cd data_selected;
for i = 1:length(List)-2
    disp(i);
    T = readtable(List(i+2,:));
    txt1 = table2array(T(:,1));t1 = table2array(T(:,4)); t2 = table2array(T(:,5)); 
    num1 = (t1(:,1)+t2(:,1))/2; 
    for j = 1:i-1
        
        if (i ~= j)
            T = readtable(List(j+2,:));
            txt2 = table2array(T(:,1));t1 = table2array(T(:,4)); t2 = table2array(T(:,5)); 
            num2 = (t1(:,1)+t2(:,1))/2; 

            cd ..;
            [price1,price2] = GetData(txt1,txt2,num1,num2);
            cd data_selected;
            
            tmp = corrcoef(price1,price2);
            R_Pearson_Table(i,j) = tmp(1,2);
            R_Spearman_Table(i,j) = corr(price1,price2,'Type','Spearman');
        end
        
    end
end
cd ..;

tmp2 = abs(R_Pearson_Table);
[tmp,list1] = sort(tmp2(:));
Max_pearson = tmp(length(tmp)-4:length(tmp));
Max_pearson_list = list1(length(list1)-4:length(list1));
Min_pearson = zeros(5);
Min_pearson_list = zeros(5);
count = 1;
for i= 5049:10000
    if (tmp(i)>0)
        Min_pearson(count) = tmp(i);
        Min_pearson_list(count) = list1(i);
        count = count +1;
        if (count >5) 
            break; end
    end
end
fprintf(fileID,'Max\r\n');
for i=1:5
    for j=1:6
        t = mod(Max_pearson_list(i),100);
        if (t==0) 
            t =100; end
        fprintf(fileID,'%c',List(t+2,j));
    end
    fprintf(fileID,' ');
    for j=1:6
        t= fix(Max_pearson_list(i)/100);
        if (mod(Max_pearson_list(i),100)==0) 
            t =t-1; end
        fprintf(fileID,'%c',List(t+3,j));
    end
    P = GetP(Max_pearson_list,i,List,'P');
    fprintf(fileID,' Pearson correlation coefficient: %f  p value:%f\r\n',Max_pearson(i),P);
end
fprintf(fileID,'Min\r\n');
for i=1:5
    for j=1:6
        t = mod(Min_pearson_list(i),100);
        if (t==0) 
            t =100; end
        fprintf(fileID,'%c',List(t+2,j));
    end
    fprintf(fileID,' ');
    for j=1:6
        t= fix(Min_pearson_list(i)/100);
        if (mod(Min_pearson_list(i),100)==0) 
            t =t-1; end
        fprintf(fileID,'%c',List(t+3,j));    
    end
    P = GetP(Min_pearson_list,i,List,'P');
    fprintf(fileID,' Pearson correlation coefficient: %f  p value:%f\r\n',Min_pearson(i),P);
end

tmp2 = abs(R_Spearman_Table);
[tmp,list1] = sort(tmp2(:));
Max_spearman = tmp(length(tmp)-4:length(tmp));
Max_spearman_list = list1(length(list1)-4:length(list1));
Min_spearman = zeros(5);
Min_spearman_list = zeros(5);
count = 1;
for i= 5049:10000
    if (tmp(i)>0)
        Min_spearman(count) = tmp(i);
        Min_spearman_list(count) = list1(i);
        count = count +1;
        if (count >5) 
            break; end
    end
end
fprintf(fileID,'Spearman Max\r\n');
for i=1:5
    for j=1:6
        t = mod(Max_spearman_list(i),100);
        if (t==0) 
            t =100; end
        fprintf(fileID,'%c',List(t+2,j));
    end
    fprintf(fileID,' ');
    for j=1:6
        t= fix(Max_spearman_list(i)/100);
        if (mod(Max_spearman_list(i),100)==0) 
            t =t-1; end
        fprintf(fileID,'%c',List(t+3,j));
    end
    P = GetP(Max_spearman_list,i,List,'S');
    fprintf(fileID,' Spearman correlation coefficient: %f  p value:%f\r\n',Max_spearman(i),P);
end
fprintf(fileID,'Min\r\n');
for i=1:5
    for j=1:6
        t = mod(Min_spearman_list(i),100);
        if (t==0) 
            t =100; end
        fprintf(fileID,'%c',List(t+2,j));
    end
    fprintf(fileID,' ');
    for j=1:6
        t= fix(Min_spearman_list(i)/100);
        if (mod(Min_spearman_list(i),100)==0) 
            t =t-1; end
        fprintf(fileID,'%c',List(t+3,j));
    end
    P = GetP(Min_spearman_list,i,List,'S');
    fprintf(fileID,' Spearman correlation coefficient: %f  p value:%f\r\n',Min_spearman(i),P);
end

R_Pearson_Table_V2 = zeros(100,100);
R_Spearman_Table_V2 = zeros(100,100);

for i=1:100
    for j=1:100
        if (i<j)
            R_Pearson_Table_V2(i,j)=R_Pearson_Table(j,i);
            R_Spearman_Table_V2(i,j)=R_Spearman_Table(j,i);
        else
             R_Pearson_Table_V2(i,j)=R_Pearson_Table(i,j);
            R_Spearman_Table_V2(i,j)=R_Spearman_Table(i,j);
        end
        if (i==j)
            R_Pearson_Table_V2(i,j) = 1;
            R_Spearman_Table_V2(i,j) = 1;
        end
    end
end
xlswrite('Pearson.xlsx',R_Pearson_Table_V2);
xlswrite('Spearman.xlsx',R_Spearman_Table_V2);
fclose(fileID);
