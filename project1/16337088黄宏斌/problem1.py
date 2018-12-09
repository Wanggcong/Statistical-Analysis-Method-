import csv
import numpy as np
import math

def read_csv(file_name):
    stock_data = []
    with open(file_name) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        stock_header = next(csv_reader)  # 读取第一行每一列的标题
        for row in csv_reader:  # 将csv 文件中的数据保存到stock_data中
            stock_data.append(row)
    return stock_header, stock_data

if __name__ == '__main__':

    file_name = "000001.csv"
    header, data = read_csv(file_name)
    high = np.array([float(x[3]) for x in data])
    low = np.array([float(x[4]) for x in data])

    n = len(low)
    price = (low+high)/2
    sort_price = sorted(price)
    avg = np.sum(price)/n
    if (n//2 == 1):
        mid = sort_price[int(n/2)]
    else:
        mid = (sort_price[int(n/2)-1]+sort_price[int(n/2)])/2

    one_fourth_index = int(n/4)
    three_fourth_index = int(3*n/4)
    one_fourth = sort_price[one_fourth_index]
    three_fourth = sort_price[three_fourth_index]

    var = (np.linalg.norm(sort_price-avg)**2)/(n-1)
    std_dev = math.sqrt(var)

    CV = std_dev/avg

    total_range = sort_price[n-1]-sort_price[0]
    one_fourth_range = sort_price[three_fourth_index+1] - sort_price[one_fourth_index]

    skewness = n/((n-1)*(n-2))*sum(np.power(sort_price-avg, 3))/std_dev**3

    kurtosis = n*(n+1)/((n-1)*(n-2)*(n-3))*sum(np.power(sort_price-avg, 4))/std_dev**4\
                - 3*(n-1)*(n-1)/((n-2)*(n-3))




    print("avarage: ", avg)
    print("mid: ", mid)
    print("one fourth: ", one_fourth)
    print("three fourth: ", three_fourth)
    print("variance: ", var)
    print("standard deviation: ", std_dev)
    print("coefficient of variation: "+str(CV*100)+"%")
    print("total range: ", total_range)
    print("one fourth range: ", one_fourth_range)
    print("skewness: ", skewness)
    print("kurtosis: ", kurtosis)

    