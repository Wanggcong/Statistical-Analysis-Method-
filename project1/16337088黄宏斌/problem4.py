import csv
import numpy as np
import math
import os
import json
import scipy.stats


def get_file_list(dir):
    file_list = []
    for file_name in os.listdir(dir):  
        if file_name[0] == '0':
            file_list.append(file_name)
    return file_list

def read_csv(file_name):
    data = []
    with open(file_name) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        stock_header = next(csv_reader)  # 读取第一行每一列的标题
        for row in csv_reader:  # 将csv 文件中的数据保存到stock_data中
            data.append(row)
    date = [(x[0]) for x in data]
    high = np.array([float(x[3]) for x in data])
    low = np.array([float(x[4]) for x in data])
    price = (low+high)/2
    return date, price

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

def Pearson(x, y):
    n = len(x)
    avg_x = sum(x)/n
    avg_y = sum(y)/n
    s_xy = (x-avg_x).dot((y-avg_y).T)/(n-1)
    s_xx = np.linalg.norm(x-avg_x)**2/(n-1)
    s_yy = np.linalg.norm(y-avg_y)**2/(n-1)
    r_xy = s_xy/math.sqrt(s_xx*s_yy)
    return r_xy

def correlation_analysis(file_name1, file_name2):
    date1, price1 = read_csv(file_name1)
    date2, price2 = read_csv(file_name2)
    n1 = len(price1)
    n2 = len(price2)
    index_list1 = []
    index_list2 = []
    i = 0
    j = 0
    while i < n1 and j < n2:
        if date1[i] == date2[j]:
            index_list1.append(i)
            index_list2.append(j)
            i += 1
            j += 1
        elif date1[i] > date2[j]:
            j += 1
        else:
            i += 1
    x = np.array([price1[i] for i in index_list1])
    y = np.array([price2[j] for j in index_list2])
    n = len(x)
    #Pearson相关系数
    r_xy = Pearson(x, y)
    #Spearman相关系数
    x_rank = compute_rank(x)
    y_rank = compute_rank(y)
    q_xy = 1-6/(n*(n*n-1))*(np.linalg.norm(x_rank-y_rank)**2)

    return r_xy, q_xy, np.array(x), np.array(y)

def save_matrix(R, file_name):
    n = len(R)
    l = [0]*n
    R_list = [l[:] for i in range(n)]
    for i in range(n):
        for j in range(n):
            R_list[i][j] = float(R[i][j])
    with open(file_name, "w") as f_json:
        json.dump(R_list, f_json)

def read_matrix(file_name):
    with open(file_name, encoding='utf8') as f_json:
        R = json.load(f_json)
    return R

def get_top_and_bottom5(R):
    n = len(R)
    max_flag = np.zeros((n,n))
    min_flag = np.zeros((n,n))
    max_pnts = []
    min_pnts = []
    for cnt in range(5):
        max_r = -1
        min_r = 2
        max_index = [-1,-1]
        min_index = [-1,-1]
        for i in range(n):
            for j in range(i):
                if (max_flag[i][j] == 0) and abs(R[i][j]) > max_r:
                    max_r = abs(R[i][j])
                    max_index = [i,j]
                    # print(i,j)
                if (min_flag[i][j] == 0) and abs(R[i][j]) < min_r:
                    min_r = abs(R[i][j])
                    min_index = [i,j]

        max_flag[max_index[0]][max_index[1]] = 1
        min_flag[min_index[0]][min_index[1]] = 1
        max_pnts.append(max_index)
        min_pnts.append(min_index)
    return max_pnts, min_pnts

def compute_p_value(r, file_name1, file_name2):
    _, _, x1, x2 = correlation_analysis(file_name1, file_name2)
    n = len(x1)
    df = 2*n-2
    t = r*math.sqrt(df/(1-r*r))
    p = 1 - scipy.stats.t.cdf(t,df=df)
    return p

def analysis_by_matrix(R, file_list, matrix_name):
    top_5, bottom_5 = get_top_and_bottom5(R)
    for i in range(5):
        max_index = top_5[i]
        max_p = compute_p_value(R[max_index[0]][max_index[1]],\
                                file_list[max_index[0]],file_list[max_index[1]])
        print(file_list[max_index[0]][:-4], "和", file_list[max_index[1]][:-4],\
               "：\t"+matrix_name+"前五相关系数：", R[max_index[0]][max_index[1]],\
               "\tp值：", max_p)
    for i in range(5):
        min_index = bottom_5[i]
        min_p = compute_p_value(R[min_index[0]][min_index[1]],\
                                file_list[min_index[0]],file_list[min_index[1]])
        print(file_list[min_index[0]][:-4], "和", file_list[min_index[1]][:-4], \
                "：\t"+matrix_name+"后五相关系数：", R[min_index[0]][min_index[1]],\
               "\tp值：", min_p)


if __name__ == '__main__':
    # 对两支股票的相关性分析
    file_name1 = "000001.csv"
    file_name2 = "000006.csv"
    r_xy, q_xy, _, _ = correlation_analysis(file_name1, file_name2)
    print("Pearson: ", r_xy)
    print("Spearman: ", q_xy)
    # 对100支股票进行两两相关性分析
    file_list = get_file_list("./") #读取csv文件名
    num = len(file_list)
    R = np.zeros((num,num))
    S = np.zeros((num,num))
    for i in range(num):
        print(i)
        for j in range(num):
            if i == j:
                R[i][j] = 1
                S[i][j] = 1
            else:
                R[i][j], S[i][j], _, _ = correlation_analysis(file_list[i], file_list[j])
                
    save_matrix(R, "R_matrix.json")
    save_matrix(S, "S_matrix.json")
    #相关性分析
    R = read_matrix("R_matrix.json")
    S = read_matrix("S_matrix.json")
    analysis_by_matrix(R, file_list, "Pearson")
    analysis_by_matrix(S, file_list, "Spearman")
