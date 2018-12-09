data =csvread('000001.csv',1,3,[1,3,4381,4]);
everydayprice = sum(data,2)/2;
average = sum(everydayprice)/4381;
fprintf('000001股票日均值：%g\n',average);  
A=sort(everydayprice);
median = A(2191);
fprintf('000001股票中位数：%g\n',median);
M025 = A(1096);%0.25*4381=1096（取整）
fprintf('000001股票M0.25分位数：%g\n',M025);
M075 = A(3286);%0.75*4381=3286
fprintf('000001股票M0.75分位数：%g\n',M075);
variance = std2(A)*std2(A); %std2求标准差
fprintf('000001股票方差：%g\n',variance);
standard_deviation = std2(A);
fprintf('000001股票标准差：%g\n',standard_deviation);
CV = std2(A)/average;
fprintf('000001股票变异系数：%g\n',CV);
rage = A(4381)-A(1);
fprintf('000001股票极差：%g\n',rage);
rage_4 = M075 - M025;
fprintf('000001股票四分位极差：%g\n',rage_4);
skewNess = skewness(A);
fprintf('000001股票偏度：%g\n',skewNess);
Kurtosis =kurtosis(A);
fprintf('000001股票峰度：%g\n',Kurtosis);

