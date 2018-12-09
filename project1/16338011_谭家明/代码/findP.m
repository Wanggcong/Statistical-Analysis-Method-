 %求出最强和最弱股票的相关性检验假设P值
stock = cell(20*2);
%读取pearson矩阵下相关性最强5对和最弱的5对股票csv文件
stock{1,1}=importdata('000046.csv');  
stock{1,2}=importdata('000069.csv');
stock{2,1}=importdata('000006.csv');
stock{2,2}=importdata('000046.csv');
stock{3,1}=importdata('000025.csv');
stock{3,2}=importdata('000567.csv');
stock{4,1}=importdata('000006.csv');
stock{4,2}=importdata('000069.csv');
stock{5,1}=importdata('000059.csv');
stock{5,2}=importdata('000708.csv');

stock{6,1}=importdata('000525.csv');
stock{6,2}=importdata('000632.csv');
stock{7,1}=importdata('000049.csv');
stock{7,2}=importdata('000090.csv');
stock{8,1}=importdata('000521.csv');
stock{8,2}=importdata('000661.csv');
stock{9,1}=importdata('000601.csv');
stock{9,2}=importdata('000661.csv');
stock{10,1}=importdata('000036.csv');
stock{10,2}=importdata('000425.csv');

%读取Spearman矩阵下相关性最强5对和最弱的5对股票csv文件
stock{11,1}=importdata('000028.csv');
stock{11,2}=importdata('000661.csv');
stock{12,1}=importdata('000025.csv');
stock{12,2}=importdata('000567.csv');
stock{13,1}=importdata('000025.csv');
stock{13,2}=importdata('000418.csv');
stock{14,1}=importdata('000423.csv');
stock{14,2}=importdata('000661.csv');
stock{15,1}=importdata('000419.csv');
stock{15,2}=importdata('000700.csv');

stock{16,1}=importdata('000563.csv');
stock{16,2}=importdata('000659.csv');
stock{17,1}=importdata('000078.csv');
stock{17,2}=importdata('000538.csv');
stock{18,1}=importdata('000001.csv');
stock{18,2}=importdata('000088.csv');
stock{19,1}=importdata('000410.csv');
stock{19,2}=importdata('000659.csv');
stock{20,1}=importdata('000425.csv');
stock{20,2}=importdata('000544.csv');

fprintf('相关性检验假设P值为：\n');
for i = 1:20
        price1 = [];
        price11 = [];
        price2 = [];
        price22 = [];
        t=1;
        C = {};
        id1 =[];
        id2 =[];
        [C,id1,id2] = intersect(stock{i,1}.textdata(:,1),stock{i,2}.textdata(:,1));
        id11 = id1';
        id22 = id2';
        for j = 1:length(id11)-1
            price1(t)=(stock{i,1}.data(id11(j)-1,3)+stock{i,1}.data(id11(j)-1,4))/2;
            price2(t)=(stock{i,2}.data(id22(j)-1,3)+stock{i,2}.data(id22(j)-1,4))/2;
            t = t+1;
        end
            price11 =price1';
            price22 =price2';
        [R,P]=corrcoef(price11,price22);
        fprintf('%f\n',P(1,2));
end
        
