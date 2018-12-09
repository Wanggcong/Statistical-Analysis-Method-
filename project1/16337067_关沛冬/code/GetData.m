%此函数用来获取相同日期的两种股票的价格
function [P1,P2] = GetData(t1,t2,n1,n2)
SameDate = intersect(t1,t2);

temp1 = containers.Map(t1,n1);
temp2 = containers.Map(t2,n2);
% temp1(SameDate(1));
 P1=zeros(length(SameDate(:,1)),1);
 P2=zeros(length(SameDate(:,1)),1);
 
tmp = 1;
while(tmp<=length(SameDate(:,1)))
    P1(tmp) = temp1(char(SameDate(tmp,1)));
    tmp = tmp + 1;
end
tmp = 1; 
while(tmp<=length(SameDate(:,1)))
    P2(tmp) = temp2(char(SameDate(tmp,1)));
    tmp = tmp + 1;
end