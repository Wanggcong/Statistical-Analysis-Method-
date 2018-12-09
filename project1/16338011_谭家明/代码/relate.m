%function M = relate() %����������ǿ�������Ĺ�Ʊ
pear = importdata('pearsonϵ��.csv'); %��ȡ�ļ�����
spear = importdata('Spearmanϵ��.csv');
Pear1 = abs(pear); %ȡ����ֵ
Pear2 = abs(pear);
Spear1 = abs(spear);
Spear2 = abs(spear);
index1 = 0;
index2 = 0;
fprintf('����pearson�����֪\n�������ǿ����Թ�Ʊλ�������ǣ�\n');
[r1,c1] = size(Pear1);
for i = 1:r1
    for j = 1:c1
        if i == j || i > j
            Pear1(i,j) = 0;  %���ظ�����λ0
        end
    end
end
    
for i = 1:5
    [index1,index2] = find(Pear1==max(max(Pear1))); %Ѱ�ҳ����������Ԫ�ص�λ��
    Pear1(index1,index2) = 0; %������0���Ա�Ѱ����һ������Ԫ��
    fprintf('%g  %g\n',index1,index2);
    index1=0;
    index2=0;
end

[r2,c2] = size(Pear2);
for i = 1:r2
    for j = 1:c2
        if i == j || i > j
            Pear2(i,j) = 1;  %��������������1
        end
    end
end
fprintf('�������������Թ�Ʊλ�������ǣ�\n');
for i = 1:5
    [index1,index2] = find(Pear2==min(min(Pear2)));%Ѱ�ҳ���������СԪ�ص�λ��
    Pear2(index1,index2) = 1;%������1���Ա�Ѱ����һ����С��Ԫ��
    fprintf('%g  %g\n',index1,index2);
    index1=0;
    index2=0;
end
fprintf('����spearman�����֪\n�������ǿ����Թ�Ʊλ�������ǣ�\n');
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
fprintf('�������������Թ�Ʊλ�������ǣ�\n');
for i = 1:5
    [index1,index2] = find(Spear2==min(min(Spear2)));
    Spear2(index1,index2) = 1;
    fprintf('%g  %g\n',index1,index2);
    index1=0;
    index2=0;
end
