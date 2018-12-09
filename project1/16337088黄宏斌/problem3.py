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

def compute_rank(array):
    sort_index = np.argsort(array)
    rank = np.zeros(len(array))
    rank_cnt = 1
    index = 0
    while index < len(sort_index):
        index1 = index
        num = array[sort_index[index1]]
        while index1+1 < len(sort_index) and array[sort_index[index1+1]] == num:
            index1 += 1
        rank_value = (2*rank_cnt+index1-index)/2
        for i in range(index, index1+1):
            rank[sort_index[i]] = rank_value
        rank_cnt += index1-index+1
        index = index1+1
    return rank


if __name__ == '__main__':
    file_name = "000012.csv"
    header, data = read_csv(file_name)
    high = np.array([float(x[3]) for x in data])
    low = np.array([float(x[4]) for x in data])
    volume = np.array([float(x[5]) for x in data])

    n = len(low)
    price = (low+high)/2
    #Pearson相关系数
    avg_x = sum(price)/n
    avg_y = sum(volume)/n
    s_xy = (price-avg_x).dot((volume-avg_y).T)/(n-1)
    s_xx = np.linalg.norm(price-avg_x)**2/(n-1)
    s_yy = np.linalg.norm(volume-avg_y)**2/(n-1)
    r_xy = s_xy/math.sqrt(s_xx*s_yy)
    #Spearman相关系数
    x_rank = compute_rank(price)
    y_rank = compute_rank(volume)
    q_xy = 1-6/(n*(n*n-1))*(np.linalg.norm(x_rank-y_rank)**2)

    print("Pearson: ", r_xy)
    print("Spearman: ", q_xy)


    