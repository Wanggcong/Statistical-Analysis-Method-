from matplotlib import pyplot as plt
import csv
import numpy as np
import scipy.stats

def read_csv(file_name):
    stock_data = []
    with open(file_name) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        stock_header = next(csv_reader)  # 读取第一行每一列的标题
        for row in csv_reader:  # 将csv 文件中的数据保存到stock_data中
            stock_data.append(row)
    return stock_header, stock_data

# 参数依次为list,抬头,X轴标签,Y轴标签,XY轴的范围，分组数
def draw_hist(myList,Title,Xlabel,Ylabel,Xmin,Xmax,Ymin,Ymax,group_num):
    plt.hist(myList,group_num)
    plt.xlabel(Xlabel)
    plt.xlim(Xmin,Xmax)
    plt.ylabel(Ylabel)
    plt.ylim(Ymin,Ymax)
    plt.title(Title)
    plt.show()

def draw_plot(myPoints,Title,Xlabel,Ylabel,Xmin,Xmax,Ymin,Ymax):
    plt.plot(myPoints[:,0],myPoints[:,1],'+')
    plt.xlabel(Xlabel)
    plt.xlim(Xmin,Xmax)
    plt.ylabel(Ylabel)
    plt.ylim(Ymin,Ymax)
    plt.title(Title)
    plt.show()

if __name__ == '__main__':
    file_name = "000006.csv"
    header, data = read_csv(file_name)
    high = np.array([float(x[3]) for x in data])
    low = np.array([float(x[4]) for x in data])

    n = len(low)
    price = (low+high)/2
    # 画直方图
    draw_hist(price,'Stock Price','price','number',0.0,40,0.0,1500,15)
    # 画QQ图
    qq_points = np.zeros((n,2))
    qq_points[:,1] = np.array(sorted(price))
    for i in range(n):
        qq_points[i][0] = scipy.stats.norm(0,1).ppf((i+1-0.375)/(n+0.25))
    draw_plot(qq_points,'QQ Gragh','x','y',-4,4,0.0,40)

    # 画差值的直方图
    difference_value = price[1:]-price[:-1]
    draw_hist(difference_value,'Difference value','value','number',-10,10,0.0,3100,15)
    #画QQ图
    d_n = len(difference_value)
    difference_value_qq_points = np.zeros((d_n,2))
    difference_value_qq_points[:,1] = np.array(sorted(difference_value))
    for i in range(d_n):
        difference_value_qq_points[i][0] = scipy.stats.norm(0,1).ppf(\
                                        (i+1-0.375)/(d_n+0.25))
    draw_plot(difference_value_qq_points,'Difference value QQ Gragh','x','y',\
                -4,4,-3.5,3.5)