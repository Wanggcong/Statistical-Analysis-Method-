function[]=sort(M1, P1)
    temp = []
    m, n = M1.shape
    for i range(m):
        j = i+1
        while j < n
            temp.append((abs(M1(i)(j)), abs(P1(i)(j))])
            j = j+1
        end
    result_list = sorted(temp, key=lambda x:(x(0),x(1)));
    print("������ص�ϵ����pֵ")
    print(result_list(0:5))
    print("��ǿ��ص�ϵ����pֵ")
    print(result_list(4945:4950))
