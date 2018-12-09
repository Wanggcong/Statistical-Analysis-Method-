function [P] = GetP(Coefficient_List,i,List,module)

P = 0;

x = fix(Coefficient_List(i,1)/100)+1;
y = mod(Coefficient_List(i,1),100);
if (y==0)
    x = x-1;
    y = 100;
end

cd data_selected;
T = readtable(List(x+2,:));
txt1 = table2array(T(:,1));t1 = table2array(T(:,4)); t2 = table2array(T(:,5)); 
num1 = (t1(:,1)+t2(:,1))/2;

T = readtable(List(y+2,:));
txt2 = table2array(T(:,1));t1 = table2array(T(:,4)); t2 = table2array(T(:,5)); 
num2 = (t1(:,1)+t2(:,1))/2; 

    cd ..;
    [price1,price2] = GetData(txt1,txt2,num1,num2);
    cd data_selected;
    
    if (module=='P')
        [~,p]=corrcoef(price1,price2);
        P = p(1,2);
    else
        [~,p] = corr(price1,price2,'Type','Spearman');
        P = p(1,1);
    end
cd ..;

% for i = 1:5
%     x = fix(Coefficient_List(i,1)/100)+1;
%     y = mod(Coefficient_List(i,1),100);
%     if (y==0)
%         x = x-1;
%         y = 100;
%     end
%     tlist(1,i*2-1) = x;
%     tlist(1,i*2,1) = y;
% end
% tlist = unique(tlist);
% disp(tlist);
% 
% cd data_selected
% for i = 1:length(tlist(1,:))
%     T = readtable(List(tlist(1,i)+2,:));
%     txt1 = table2array(T(:,1));t1 = table2array(T(:,4)); t2 = table2array(T(:,5)); 
%     num1 = (t1(:,1)+t2(:,1))/2;
%     for j=1:length(tlist(1,:))
%         T = readtable(List(tlist(1,j)+2,:));
%         txt2 = table2array(T(:,1));t1 = table2array(T(:,4)); t2 = table2array(T(:,5)); 
%         num2 = (t1(:,1)+t2(:,1))/2; 
%     
%     cd ..;
%     [price1,price2] = GetData(txt1,txt2,num1,num2);
%     cd data_selected;
%     
%     if (module=='P')
%         [~,p]=corrcoef(price1,price2);
%         P(i,j) = p(1,2);
%     else
%         [~,p] = corr(price1,price2,'Type','Spearman');
%         P(i,j) = p(1,1);
%     end
%     
%     
%     %Q(i,j) = q(1,2);
%     Nog(i,:) = strtok(List(tlist(1,i)+2,:),'.');
%     %Nog(i,:) = strtok(Nog(i,:),'.');
%     end
% end
% cd ..;