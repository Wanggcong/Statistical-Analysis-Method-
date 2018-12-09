function[dp1,dp2]=getSameDate(csv_data1,csv_data2)
d1, p1 = getDatePrice(csv_data1);
d2, p2 = getDatePrice(csv_data2);
i = 0
j = 0
while i < len(d1) && j < len(d2)
    if d1(i) == d2(j)
        dp1(end+1)=p1(i);
        dp2(end+1)=p2(j);
        i = i+1;
        j = j+1;
    elseif d1(i) < d2(j):
        i = i+1;
    else
        j = j+1;
    end
end