import csv
import pygal
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

file_name = 'data_selected/000006.csv'

price = []
diff_price = []
with open(file_name) as infile:
    reader = csv.reader(infile)
    header_row = next(reader)  # 去除表头

    # 第1行
    first_line = next(reader)
    price.append((float(first_line[3])+float(first_line[4]))/2)

    # 第2-n行
    for row in reader:  # 在读取时,输入数据的每一行都被解析并转换为字符串列表
        price.append((float(row[3])+float(row[4]))/2)
        diff_price.append(price[-1]-price[-2])

price = np.array(price, dtype=float)
diff_price = np.array(diff_price, dtype=float)

max1 = np.max(price)  # 38.055
min1 = np.min(price)  # 3.295
max2 = np.max(diff_price)
min2 = np.min(diff_price)


# 计算价格的直方图
# 10组,组距为4,[0,4),[4,8),...,[36,40)
group_size = 4
lower_bound = int(min1//group_size)
upper_bound = int(max1//group_size)+1
hist = np.zeros((upper_bound-lower_bound), dtype=float)
for p in price:
    hist[int(p//group_size)] += 1
hist = hist/price.size  # 归一化

# 直方图横轴标签
label = []
for i in range(lower_bound, upper_bound):
    tmp = '['+str(i*group_size)+','+str((i+1)*group_size)+')'
    label.append(tmp)

# 使用pygal画出直方图
bar = pygal.Bar()
bar.x_labels = label
bar.x_title = "Price"
bar.y_title = "Frequency"
bar.add(None, hist)
bar.render_to_file("histogram1.svg")


# 计算差价的直方图
# 16组,组距为1,[-13,-12),[-12,-11),...,[2,3)
lower_bound = int(min2//1)
upper_bound = int(max2//1)+1
hist2 = np.zeros((upper_bound-lower_bound), dtype=float)
for p in diff_price:
    hist2[int(p//1)-lower_bound] += 1
hist2 = hist2/diff_price.size  # 归一化

# 直方图横轴标签
label2 = []
for i in range(lower_bound, upper_bound):
    tmp = '['+str(i)+','+str(i+1)+')'
    label2.append(tmp)

# 使用pygal画出直方图
bar2 = pygal.Bar()
bar2.x_labels = label2
bar2.x_title = "Price Difference"
bar2.y_title = "Frequency"
bar2.add(None, hist2)
bar2.render_to_file("histogram2.svg")


# 画价格和差值QQ图
sorted_price = np.sort(price)
sorted_diff_price = np.sort(diff_price)

plt.figure(1)
n = sorted_price.size
for i in range(0, n, 10):
    plt.scatter(norm.ppf((i-0.375)/(n+0.25)), sorted_price[i], s=1)
# plt.plot([-5, 5], [-5*var1+avg1, 5*var1+avg1])
plt.savefig("fig1.jpg")

plt.figure(2)
n = sorted_diff_price.size
for i in range(0, n, 10):
    plt.scatter(norm.ppf((i-0.375)/(n+0.25)), sorted_diff_price[i], s=1)
# plt.plot([-5, 5], [-5*var2+avg2, 5*var2+avg2])
plt.savefig("fig2.jpg")
