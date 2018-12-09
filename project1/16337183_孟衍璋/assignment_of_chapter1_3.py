import pandas as pd
from scipy import stats
import math

def sum_element(a):
	sum = 0
	for i in a:
		sum += i
	return sum

f = pd.read_csv("000012.csv")

# 每日股价 = （每日最低价+每日最高价）/ 2
daily_stock_price = ((f.high + f.low) / 2).tolist()

# 股票000001历史股价的日均值(所有天数的股价求平均)
daily_average = sum_element(daily_stock_price) / f.shape[0]

# 成交量
volume = f.volume.tolist()

# 成交量的平均数
volume_average = sum_element(volume) / f.shape[0]

# pearson相关系数
print(stats.pearsonr(daily_stock_price, volume))
# (0.0298159151939864, 0.04726388233143951)
# temp = 0
# for i in range(f.shape[0]):
# 	temp += (daily_stock_price[i] - daily_average) * (volume[i] - volume_average)
# Sxy = temp / (f.shape[0] - 1)

# Sxx = sum_element([(x - daily_average) ** 2 for x in daily_stock_price]) / (f.shape[0] - 1)
# Syy = sum_element([(y - volume_average) ** 2 for y in volume]) / (f.shape[0] - 1)

# rxy = Sxy / (math.sqrt(Sxx) * math.sqrt(Syy))
# print("Pearson correlation coefficient =", rxy)

# spearman相关系数
print(stats.spearmanr(daily_stock_price, volume))
# SpearmanrResult(correlation=-0.018695952028035114, pvalue=0.2135561392338957)

# daily_stock_price_sorted = sorted(daily_stock_price)
# volume_sorted = sorted(volume)

# R = list()
# S = list()
# for i in range(f.shape[0]):
# 	R.append(daily_stock_price_sorted.index(daily_stock_price[i]))
# 	S.append(volume_sorted.index(volume[i]))

# total = 0
# for i in range(f.shape[0]):
# 	total += (R[i] - S[i]) ** 2
# qxy = 1 - float(6 * total) / (f.shape[0] * (f.shape[0] ** 2 - 1))
# print("Spearman correlation coefficient =", qxy)