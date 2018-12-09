import datetime
import numpy as np
import matplotlib.pyplot as plt


def load_data(fname1, fname2):
    price_pair = []
    with open(fname1) as infile1, open(fname2) as infile2:
        next(infile1)
        next(infile2)  # 去除表头
        lines1 = infile1.readlines()
        lines2 = infile2.readlines()

        n1, n2 = len(lines1), len(lines2)
        i, j = 0, 0
        while i < n1 and j < n2:
            lin1 = lines1[i].split(',')
            lin2 = lines2[j].split(',')
            tmp = lin1[0].split('-')
            day1 = datetime.date(int(tmp[0]), int(tmp[1]), int(tmp[2]))
            tmp = lin2[0].split('-')
            day2 = datetime.date(int(tmp[0]), int(tmp[1]), int(tmp[2]))
            if day1 == day2:  # 找到相同的日期
                price_pair.append(
                    [(float(lin1[3])+float(lin1[4]))/2, (float(lin2[3])+float(lin2[4]))/2])
                i = i+1
                j = j+1
            elif day1 < day2:
                i = i+1
            else:
                j = j+1

    price_pair = np.array(price_pair, dtype=float)
    return price_pair


def compute_pearson(price_pair):
    # 计算pearson相关系数
    avg_price = np.average(price_pair, axis=0)
    var1, var2, cov = 0.0, 0.0, 0.0
    n = price_pair.shape[0]
    for i in range(n):
        var1 += (price_pair[i, 0]-avg_price[0])**2
        var2 += (price_pair[i, 1]-avg_price[1])**2
        cov += (price_pair[i, 0]-avg_price[0])*(price_pair[i, 1]-avg_price[1])

    pearson = cov/np.sqrt(var1*var2)
    return pearson


def compute_spearman(price_pair):
    # 构造次序统计量
    sorted_arg = np.argsort(price_pair, axis=0)
    order_stat = np.zeros_like(price_pair)
    for i in range(sorted_arg.shape[0]):
        order_stat[sorted_arg[i, 0], 0] = i+1
        order_stat[sorted_arg[i, 1], 1] = i+1

    avg_x = np.average(order_stat, axis=0)
    var1, var2, cov = 0.0, 0.0, 0.0
    n = order_stat.shape[0]
    for i in range(n):
        var1 += (order_stat[i, 0]-avg_x[0])**2
        var2 += (order_stat[i, 1]-avg_x[1])**2
        cov += (order_stat[i, 0]-avg_x[0])*(order_stat[i, 1]-avg_x[1])

    spearman = cov/np.sqrt(var1*var2)
    return spearman


if __name__ == "__main__":
    fname1 = 'data_selected/000001.csv'
    fname2 = 'data_selected/000006.csv'
    price_pair = load_data(fname1, fname2)

    pearson = compute_pearson(price_pair)
    print("Pearson相关系数 = \n", pearson)
    spearman = compute_spearman(price_pair)
    print("Spearman相关系数 = \n", spearman)
