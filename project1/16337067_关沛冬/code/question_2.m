[~,txt] = xlsread('\data_selected\000006.csv','A:A');
num = xlsread('\data_selected\000006.csv','B:G'); 

Price=zeros(length(num(:,1)),1);
for i = 1:length(num(:,1))
    Price(i,1) = (num(i,3)+num(i,4))/2;
end

Max = max(Price);
Minimum = min(Price);
Range = Max - Minimum;

edges1 = [0 0:0.5:40 40];
h = histogram(Price,edges1);
qqplot(Price);
% �ɼ���������̬�ֲ����壬QQͼ�����㲻��ֱ�߸���

sub = zeros(length(Price)-1,1);
for i = 1:length(Price)-1
    sub(i,1) = Price(i+1,1) - Price(i,1);
    if (sub(i,1)>1.8||sub(i,1)<-1.8) disp(sub(i,1)); end
end

Max = max(sub);
Minimum = min(sub);
Range = Max - Minimum;

edges = [-2.4 -2.4:0.07:2.4 2.4];
h3 = histogram(sub,edges);
h3 = histogram(sub);
h2 = histogram(sub);
qqplot(sub);

% �ɼ۵Ĳ�ֵҲ��������̬�ֲ�����ΪQQͼ��ɢ��ͼ�������ģ�������QQͼ��̬�ֲ�����ʱ������