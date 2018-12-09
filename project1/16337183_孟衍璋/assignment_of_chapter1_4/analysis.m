%找到绝对值最接近1的5个数
%pearson
[value1,indice1]=sort(abs(pearson_matrix(:)),'descend');
[Xaxis1,Yaxis1]=find(pearson_matrix>=value1(5));
%spearman
[value_s1,indice_s1]=sort(abs(spearman_matrix(:)),'descend');
[Xaxis_s1,Yaxis_s1]=find(spearman_matrix>=value_s1(5));

%找到绝对值最接近0的5个数
%pearson
[value2,indice2]=sort(abs(pearson_matrix(:)));
value2 = nonzeros(value2);

Xaxis2 = zeros(5,1);
Yaxis2 = zeros(5,1);

for k = 1:5
    [x,y]=find(pearson_matrix==value2(k) | pearson_matrix==-value2(k));
    Xaxis2(k) = x;
    Yaxis2(k) = y;
end
%spearman
[value_s2,indice_s2]=sort(abs(spearman_matrix(:)));
value_s2 = nonzeros(value_s2);

Xaxis_s2 = zeros(5,1);
Yaxis_s2 = zeros(5,1);

for j = 1:5
    [xs,ys]=find(spearman_matrix==value_s2(j) | spearman_matrix==-value_s2(j));
    Xaxis_s2(j) = xs;
    Yaxis_s2(j) = ys;
end


[r1,p1] = calculate_pearson('000006.csv', '000046.csv');
[r2,p2] = calculate_pearson('000006.csv', '000069.csv');
[r3,p3] = calculate_pearson('000046.csv', '000069.csv');
[r4,p4] = calculate_pearson('000025.csv', '000567.csv');
[r5,p5] = calculate_pearson('000059.csv', '000708.csv');
[r6,p6] = calculate_pearson('000525.csv', '000632.csv');
[r7,p7] = calculate_pearson('000049.csv', '000090.csv');
[r8,p8] = calculate_pearson('000521.csv', '000661.csv');
[r9,p9] = calculate_pearson('000601.csv', '000661.csv');
[r10,p10] = calculate_pearson('000036.csv', '000425.csv');

[s1,sp1] = calculate_spearman('000025.csv', '000418.csv');
[s2,sp2] = calculate_spearman('000025.csv', '000567.csv');
[s3,sp3] = calculate_spearman('000028.csv', '000661.csv');
[s4,sp4] = calculate_spearman('000423.csv', '000661.csv');
[s5,sp5] = calculate_spearman('000421.csv', '000702.csv');
[s6,sp6] = calculate_spearman('000567.csv', '000667.csv');
[s7,sp7] = calculate_spearman('000088.csv', '000538.csv');
[s8,sp8] = calculate_spearman('000001.csv', '000088.csv');
[s9,sp9] = calculate_spearman('000418.csv', '000667.csv');
[s10,sp10] = calculate_spearman('000425.csv', '000548.csv');