import csv
import numpy as np

file_name = 'data_selected/000006.csv'

price = []
with open(file_name) as infile:
    reader = csv.reader(infile)
    header_row = next(reader)  # 去除表头
    for row in reader:  # 在读取时,输入数据的每一行都被解析并转换为字符串列表
        price.append((float(row[3])+float(row[4]))/2)
price = np.array(price, dtype=float)
n = price.size

avg = np.average(price)
percent = np.percentile(price, [0, 25, 50, 75, 100])
print("均值 = ", avg)
print("最小值 = ", percent[0])
print("最大值 = ", percent[4])
print("中值 = ", percent[2])
print("下四分位点 = ", percent[1])
print("上四分位点 = ", percent[3])
print("极差 = ", percent[4]-percent[0])
print("四分位极差 = ", percent[3]-percent[1])

variance = 0.0
for i in range(n):
    variance += (price[i]-avg)**2
variance /= (n-1)
print("方差 = ", variance)

std_deviation = np.sqrt(variance)
print("标准差 = ", std_deviation)

print("变异系数 = " + str(std_deviation/avg*100) + "%")

g1 = 0.0
for i in range(n):
    g1 += (price[i]-avg)**3
g1 = g1*n/((n-1)*(n-2)*std_deviation**3)
print("偏度 = ", g1)

g2 = 0.0
for i in range(n):
    g2 += (price[i]-avg)**4
g2 = g2*n*(n+1)/((n-1)*(n-2)*(n-3)*variance**2)-3*(n-1)**2/((n-2)*(n-3))
print("峰度 = ", g2)
