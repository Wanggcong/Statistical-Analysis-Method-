data =csvread('000001.csv',1,3,[1,3,4381,4]);
everydayprice = sum(data,2)/2;
average = sum(everydayprice)/4381;
fprintf('000001��Ʊ�վ�ֵ��%g\n',average);  
A=sort(everydayprice);
median = A(2191);
fprintf('000001��Ʊ��λ����%g\n',median);
M025 = A(1096);%0.25*4381=1096��ȡ����
fprintf('000001��ƱM0.25��λ����%g\n',M025);
M075 = A(3286);%0.75*4381=3286
fprintf('000001��ƱM0.75��λ����%g\n',M075);
variance = std2(A)*std2(A); %std2���׼��
fprintf('000001��Ʊ���%g\n',variance);
standard_deviation = std2(A);
fprintf('000001��Ʊ��׼�%g\n',standard_deviation);
CV = std2(A)/average;
fprintf('000001��Ʊ����ϵ����%g\n',CV);
rage = A(4381)-A(1);
fprintf('000001��Ʊ���%g\n',rage);
rage_4 = M075 - M025;
fprintf('000001��Ʊ�ķ�λ���%g\n',rage_4);
skewNess = skewness(A);
fprintf('000001��Ʊƫ�ȣ�%g\n',skewNess);
Kurtosis =kurtosis(A);
fprintf('000001��Ʊ��ȣ�%g\n',Kurtosis);

