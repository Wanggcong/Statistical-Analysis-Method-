import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import pylab
import os
import time
from multiprocessing import Process, Pool

#定义中文字体
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
#定义输出格式
pd.set_option('max_columns', 100)
pd.set_option('max_rows', 100)
pd.set_option('display.width',200)
pd.set_option('display.max_colwidth',100)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True)

#part1
data_000001 = pd.read_csv('./data_selected/000001.csv')
f = open("./answer1.txt", 'w')
#中位数 25% 50% 标准差 日均值 75%
price_000001 = (data_000001['high'] + data_000001['low']) / 2;
result = price_000001.describe(include = [np.number])
#方差
result.loc['var'] = price_000001.var()
#极差 变异系数 四分位极差 偏度 峰度
result.loc['range'] =  result.loc['max'] - result.loc['min']
result.loc['cv'] = result.loc['std'] / result.loc['mean']
result.loc['quartile_deviation'] = result.loc['75%'] - result.loc['25%']
result.loc['skew'] = result.skew()
result.loc['kurt'] = result.kurt()
print(result, file = f)
f.close()

#part2
data_000006 = pd.read_csv('./data_selected/000006.csv')
#part2.1
price_000006 = (data_000006['high'] + data_000006['low'])/2;
plt.hist(price_000006, bins = 50, density = True)
plt.title('000006 股价')
plt.xlabel('股价')
plt.ylabel('频率')
plt.savefig('2.1.png')
plt.close()
#part2.2
stats.probplot(price_000006, dist="norm", plot=pylab)
pylab.savefig('2.2.png')
pylab.close()
#part2.3
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
plt.hist(price_000006.diff().dropna(), range=(-3,3), bins=200, density=True)
plt.title('000006 股价差值')
plt.xlabel('股价差值')
plt.ylabel('频率')
plt.savefig('2.3.png')
plt.close()
#part2.4
stats.probplot(price_000006.diff().dropna(), dist="norm", plot=pylab)
pylab.savefig('2.4.png')

#part3
data_000012 = pd.read_csv('./data_selected/000012.csv')
data_000012['price'] = (data_000012['high'] + data_000012['low'])/2
data_000012 = data_000012[['price', 'volume']]

f = open("./answer3.txt", 'w')
print("000012的股价和成交量的Pearson相关系数\n", data_000012.corr(), "\n\n", "000012的股价和成交量的Spearman相关系数\n", data_000012.corr('spearman'), file = f)
f.close()

#part4
#定义输出文件
f = open("./answer4.txt", 'w')

#并发计算系数矩阵
def cal_matrix(Data, lower_bound, upper_bound, file_index, Process_index):
    start_time = time.time()
    result_pearson = np.zeros((upper_bound - lower_bound, upper_bound))
    result_pearson_array = []
    result_spearman = np.zeros((upper_bound - lower_bound, upper_bound))
    result_spearman_array = []

    for x in range(0, upper_bound - lower_bound):
        for y in range(0, x + lower_bound):
            union = pd.merge(Data[x + lower_bound], Data[y], on="date", suffixes=('_left', '_right'))
            union['left_price'] = (union['high_left'] + union['low_left'])/2
            union['right_price'] = (union['high_right'] + union['low_right']) /2
            union = union[['left_price', 'right_price']]
            result_pearson[x][y] = union.corr()['left_price']['right_price']
            result_pearson_array.append(abs(result_pearson[x][y]))
            result_spearman[x][y] = union.corr('spearman')['left_price']['right_price']
            result_spearman_array.append(abs(result_spearman[x][y]))

    temp = pd.DataFrame(result_pearson, index = file_index[lower_bound:upper_bound], columns= file_index[:upper_bound])
    temp.to_csv('Pearson' + str(Process_index) + '.csv')
    temp = pd.DataFrame(result_spearman, index = file_index[lower_bound:upper_bound], columns=file_index[:upper_bound])
    temp.to_csv('Spearman' + str(Process_index) + '.csv')
    end_time = time.time()
    print("Process " , Process_index, " run ", end_time- start_time,  " s\n" )
    return [result_pearson_array, result_spearman_array]

if __name__ == '__main__':
    L = []
    # root_dir为要读取文件的根目录
    root_dir = r"./data_selected"
    file_index = []
    # 读取批量文件后要写入的文件
    # 依次读取根目录下的每一个文件
    for file in os.listdir(root_dir):
        file_name = root_dir + "/" + file
        L.append(pd.read_csv(file_name))
        file_index.append(file[:6])
    # 对所有股票两两求相关系数，并组合成相关系数矩阵
    record = []
    lower_bound = [0, 50, 70, 87]
    upper_bound = [50, 70, 87, 100]
    #计算累积数列
    temp = 0
    bound_list = []
    for i in range(1, 100):
        temp += i
        bound_list.append(temp)
    #并发计算
    pool = Pool(processes=4)
    for i in range(4):
        record.append(pool.apply_async(cal_matrix, args=(L, lower_bound[i], upper_bound[i], file_index, i)))
    pool.close()
    pool.join()
    #合并并行计算的结果
    sub_pearson_array = []
    sub_spearman_array = []
    for i in record:
        sub_pearson_array.append(i.get()[0])
        sub_spearman_array.append(i.get()[1])
    pearson_array = np.concatenate((sub_pearson_array[0], sub_pearson_array[1], sub_pearson_array[2], sub_pearson_array[3]))
    spearman_array = np.concatenate((sub_spearman_array[0], sub_spearman_array[1], sub_spearman_array[2], sub_spearman_array[3]))
    #合并csv
    pearson_csv = []
    spearman_csv = []
    for i in range(4):
        pearson_csv.append(pd.read_csv('Pearson' + str(i) + '.csv'))
        spearman_csv.append(pd.read_csv('Spearman' + str(i) + '.csv'))
    csv1 = pd.concat(pearson_csv, sort=False)
    csv2 = pd.concat(spearman_csv, sort=False)
    csv1.to_csv('Pearson.csv', index=False)
    csv2.to_csv('Spearman.csv', index=False)

##找出相关性最强和相关性最弱的5组股票
    index_pearson_sort_list = pearson_array.argsort()
    index_spearman_sort_list = spearman_array.argsort()
    max_pearson_num_index_list = index_pearson_sort_list[-5:][::-1]
    min_pearson_num_index_list = index_pearson_sort_list[:5][:]
    max_spearman_num_index_list = index_spearman_sort_list[-5:][::-1]
    min_spearman_num_index_list = index_spearman_sort_list[:5][:]
    print("由Pearson系数矩阵可得，相关性最强的5对股票的Pearson相关系数及其p值为：\n 股票A  股票B   Pearson系数   p值", file=f)
    for i in range(5):
        for j in range(100):
            if max_pearson_num_index_list[i] < bound_list[j]:
                data_a = pd.read_csv(root_dir + '/' + file_index[j+1] + '.csv')
                data_b = pd.read_csv(root_dir + '/' + file_index[max_pearson_num_index_list[i] % bound_list[j-1]] + '.csv')
                union = pd.merge(data_a, data_b, on="date", suffixes=('_left', '_right'))
                union['price_left'] = (union['high_left'] + union['low_left']) / 2
                union['price_right'] = (union['high_right'] + union['low_right']) / 2
                (pearson , pvalue) = stats.pearsonr(union['price_left'], union['price_right'])
                print(file_index[j + 1], file_index[max_pearson_num_index_list[i] % bound_list[j - 1]], format(union.corr()['price_left']['price_right'] , '0.10f'), format(pvalue, '0.5f'), file =f)
                break;
    print("由Pearson系数矩阵可得，相关性最弱的5对股票的Pearson相关系数及其p值为：\n 股票A  股票B   Pearson系数   p值", file=f)
    for i in range(5):
        for j in range(100):
            if min_pearson_num_index_list[i] < bound_list[j]:
                data_a = pd.read_csv(root_dir + '/' + file_index[j+1] + '.csv')
                data_b = pd.read_csv(root_dir + '/' + file_index[min_pearson_num_index_list[i] % bound_list[j-1]] + '.csv')
                union = pd.merge(data_a, data_b, on="date", suffixes=('_left', '_right'))
                union['price_left'] = (union['high_left'] + union['low_left']) / 2
                union['price_right'] = (union['high_right'] + union['low_right']) / 2
                (pearson, pvalue) = stats.pearsonr(union['price_left'], union['price_right'])
                print(file_index[j + 1], file_index[min_pearson_num_index_list[i] % bound_list[j - 1]],  format(union.corr()['price_left']['price_right'], '0.10f'), format(pvalue, '0.5f'), file =f)
                break;
    print("由Spearman系数矩阵可得，相关性最强的5对股票的Spearman相关系数及其p值为：\n 股票A  股票B   Spearman系数   p值", file=f)
    for i in range(5):
        for j in range(100):
            if max_spearman_num_index_list[i] < bound_list[j]:
                data_a = pd.read_csv(root_dir + '/' + file_index[j+1] + '.csv')
                data_b = pd.read_csv(root_dir + '/' + file_index[max_spearman_num_index_list[i] % bound_list[j-1]] + '.csv')
                union = pd.merge(data_a, data_b, on="date", suffixes=('_left', '_right'))
                union['price_left'] = (union['high_left'] + union['low_left']) / 2
                union['price_right'] = (union['high_right'] + union['low_right']) / 2
                (spearman, pvalue) = stats.spearmanr(union['price_left'], union['price_right'])
                print(file_index[j + 1], file_index[max_spearman_num_index_list[i] % bound_list[j - 1]], format( union.corr('spearman')['price_left']['price_right'] , '0.10f'), format(pvalue, '0.5f'), file =f)
                break;
    print("由Spearman系数矩阵可得，相关性最强的5对股票的Spearman相关系数及其p值为：\n 股票A  股票B   Spearman系数   p值", file=f)
    for i in range(5):
        for j in range(100):
            if min_spearman_num_index_list[i] < bound_list[j]:
                data_a = pd.read_csv(root_dir + '/' + file_index[j+1] + '.csv')
                data_b = pd.read_csv(root_dir + '/' + file_index[min_spearman_num_index_list[i] % bound_list[j-1]] + '.csv')
                union = pd.merge(data_a, data_b, on="date", suffixes=('_left', '_right'))
                union['price_left'] = (union['high_left'] + union['low_left']) / 2
                union['price_right'] = (union['high_right'] + union['low_right']) / 2
                (spearman, pvalue) = stats.spearmanr(union['price_left'], union['price_right'])
                print(file_index[j + 1], file_index[min_spearman_num_index_list[i] % bound_list[j - 1]], format(union.corr('spearman')['price_left']['price_right'], '0.10f'), format(pvalue, '0.5f'), file =f)
                break;

