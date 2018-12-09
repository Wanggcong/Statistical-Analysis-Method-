import csv
import numpy as np
import matplotlib.pyplot as plt


def load_data(file_name):
    sample = []
    with open(file_name) as infile:
        reader = csv.reader(infile)
        header_row = next(reader)  # 去除表头

        for row in reader:  # 在读取时,输入数据的每一行都被解析并转换为字符串列表
            price = (float(row[3])+float(row[4]))/2
            volume = float(row[5])
            sample.append([price, volume])

    sample = np.array(sample, dtype=float)
    return sample


def compute_pearson(sample):
    n = sample.shape[0]  # size
    avg_x = np.average(sample, axis=0).reshape(2, 1)

    cov_mat = np.zeros((2, 2), dtype=float)  # 协方差矩阵
    for i in range(n):
        x = sample[i].reshape(2, 1)
        cov_mat += np.matmul((x-avg_x), (x-avg_x).T)
    cov_mat = cov_mat/(n-1)

    variance = np.var(sample, axis=0)
    variance = variance/(n-1)*n  # 样本方差

    diag = np.diag((np.power(variance[0], -1/2), np.power(variance[1], -1/2)))
    pearson_mat = np.matmul(np.matmul(diag, cov_mat), diag)

    # 画图直观感受股价和成交量的相关性
    plt.figure()
    plt.scatter(sample[:, 0], sample[:, 1], s=1)
    plt.savefig('fig3.jpg')

    return cov_mat, pearson_mat


def compute_spearman(sample):
    n = sample.shape[0]  # size
    # 构造次序统计量
    sorted_arg = np.argsort(sample, axis=0)
    order_stat = np.zeros_like(sample)
    for i in range(n):
        order_stat[sorted_arg[i, 0], 0] = i+1
        order_stat[sorted_arg[i, 1], 1] = i+1

    avg_x = np.average(order_stat, axis=0).reshape(2, 1)

    cov_mat = np.zeros((2, 2), dtype=float)
    for i in range(n):
        x = order_stat[i].reshape(2, 1)
        cov_mat += np.matmul((x-avg_x), (x-avg_x).T)
    cov_mat = cov_mat/(n-1)

    variance = np.var(order_stat, axis=0)
    variance = variance/(n-1)*n

    diag = np.diag((np.power(variance[0], -1/2), np.power(variance[1], -1/2)))
    spearman_mat = np.matmul(np.matmul(diag, cov_mat), diag)

    # 画图直观感受股价和成交量的相关性
    plt.figure()
    plt.scatter(order_stat[:, 0], order_stat[:, 1], s=1)
    plt.savefig('fig4.jpg')

    return spearman_mat


if __name__ == "__main__":
    file_name = 'data_selected/000012.csv'
    sample = load_data(file_name)

    cov_mat, pearson_mat = compute_pearson(sample)
    print("covariance = \n", cov_mat)
    print("Pearson = \n", pearson_mat)

    spearman_mat = compute_spearman(sample)
    print("Spearman = \n", spearman_mat)
