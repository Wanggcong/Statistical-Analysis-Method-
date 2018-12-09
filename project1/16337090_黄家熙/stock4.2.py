import glob
import datetime
import numpy as np
from scipy.stats import pearsonr, spearmanr


def analysis(fname1, fname2):
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
            if day1 == day2:
                price_pair.append(
                    [(float(lin1[3])+float(lin1[4]))/2, (float(lin2[3])+float(lin2[4]))/2])
                i = i+1
                j = j+1
            elif day1 < day2:
                i = i+1
            else:
                j = j+1

    price_pair = np.array(price_pair, dtype=float)
    pearson, pp = pearsonr(price_pair[:, 0], price_pair[:, 1])
    spearman, sp = spearmanr(price_pair[:, 0], price_pair[:, 1])
    return pearson, pp, spearman, sp


def max_min(mat, n):
    tri_mat = []  # 取相关矩阵的下三角部分且不包括对角线
    for i in range(1, n):
        for j in range(0, i):
            tri_mat.append(abs(mat[i, j]))  # 取绝对值
    tri_mat = np.array(tri_mat, dtype=float)

    arg = np.argsort(tri_mat)  # 对下标进行排序
    min_index = arg[0:5]  # 取最小的5个相关系数
    print(min_index)
    max_index = arg[-5:]  # 取最大的5个相关系数
    print(max_index)

    help_index = []  # 辅助计算下标在原始相关系数矩阵的位置
    tmp = 0
    for i in range(n-1):
        tmp += i
        help_index.append(tmp)

    min_pair = []  # 相关性最弱的5对股票
    for index in min_index:
        for i in range(n-1):
            if index < help_index[i]:
                stock1 = i-1
                stock2 = index-help_index[i-1]
                min_pair.append([stock1+2, stock2+1])
                break
            elif index >= help_index[n-2]:
                stock1 = n-2
                stock2 = index-help_index[n-2]
                min_pair.append([stock1+2, stock2+1])
                break
    print(min_pair)

    max_pair = []  # 相关性最强的5对股票
    for index in max_index[::-1]:
        for i in range(n-1):
            if index < help_index[i]:
                stock1 = i-1
                stock2 = index-help_index[i-1]
                max_pair.append([stock1+2, stock2+1])
                break
            elif index >= help_index[n-2]:
                stock1 = n-2
                stock2 = index-help_index[n-2]
                max_pair.append([stock1+2, stock2+1])
                break
    print(max_pair)
    return min_pair, max_pair


if __name__ == "__main__":
    file_name_set = glob.glob('data_selected/*.csv')  # 读入所有csv文件
    n = len(file_name_set)
    # n = 20
    Pearson_mat = np.ones((n, n), dtype=float)
    pp_mat = np.ones((n, n), dtype=float)
    Spearman_mat = np.ones((n, n), dtype=float)
    sp_mat = np.ones((n, n), dtype=float)
    for i in range(n):
        for j in range(i+1, n):
            print("i=", i, ", j=", j)
            # 选取相同日期的股价,计算相关系数并返回
            pearson, pp, spearman, sp = analysis(
                file_name_set[i], file_name_set[j])
            Pearson_mat[i, j] = pearson
            Pearson_mat[j, i] = pearson
            pp_mat[i, j] = pp
            pp_mat[j, i] = pp
            Spearman_mat[i, j] = spearman
            Spearman_mat[j, i] = spearman
            sp_mat[i, j] = sp
            sp_mat[j, i] = sp

    # 计算相关性最强和最弱的5对股票
    min_pair1, max_pair1 = max_min(Pearson_mat, n)
    min_pair2, max_pair2 = max_min(Spearman_mat, n)

    print("Pearson相关性最弱")
    for p in min_pair1:
        f1 = file_name_set[p[0]-1][14:20]
        f2 = file_name_set[p[1]-1][14:20]
        r = Pearson_mat[p[0]-1, p[1]-1]
        pp = pp_mat[p[0]-1, p[1]-1]
        print(f1, f2, r, pp, sep='  ')
    print("Pearson相关性最强")
    for p in max_pair1:
        f1 = file_name_set[p[0]-1][14:20]
        f2 = file_name_set[p[1]-1][14:20]
        r = Pearson_mat[p[0]-1, p[1]-1]
        pp = pp_mat[p[0]-1, p[1]-1]
        print(f1, f2, r, pp, sep='  ')

    print("Spearman相关性最弱")
    for p in min_pair2:
        f1 = file_name_set[p[0]-1][14:20]
        f2 = file_name_set[p[1]-1][14:20]
        r = Spearman_mat[p[0]-1, p[1]-1]
        sp = sp_mat[p[0]-1, p[1]-1]
        print(f1, f2, r, sp, sep='  ')
    print("Spearman相关性最强")
    for p in max_pair2:
        f1 = file_name_set[p[0]-1][14:20]
        f2 = file_name_set[p[1]-1][14:20]
        r = Spearman_mat[p[0]-1, p[1]-1]
        sp = sp_mat[p[0]-1, p[1]-1]
        print(f1, f2, r, sp, sep='  ')
