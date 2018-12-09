# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import math

def sum_element(a):
	sum = 0
	for i in a:
		sum += i
	return sum

# 判断一个数是否为整数
def judge_int(a):
	if(a == int(a)):
		return 1
	return 0

f = pd.read_csv('000001.csv')

# 每日股价 = （每日最低价+每日最高价）/ 2
daily_stock_price = ((f.high + f.low) / 2).tolist()

# 股票000001历史股价的日均值(所有天数的股价求平均)
daily_average = sum_element(daily_stock_price) / f.shape[0]
print("daily_average =",daily_average)

daily_stock_price.sort()

# 中位数
if(f.shape[0] % 2 == 0):
	median = (daily_stock_price[int(f.shape[0] / 2)] + daily_stock_price[int(f.shape[0] / 2 - 1)]) / 2
else:
	median = daily_stock_price[int((f.shape[0] - 1) / 2)]
print("median =", median)

# 0.25分位数
p = f.shape[0] * 0.25
if(judge_int(p)):
	quantile_025 = (daily_stock_price[p] + daily_stock_price[p - 1]) / 2
else:
	quantile_025 = daily_stock_price[math.floor(p)]
print("quantile_025 =", quantile_025)

# 0.75分位数
p = f.shape[0] * 0.75
if(judge_int(p)):
	quantile_075 = (daily_stock_price[p] + daily_stock_price[p - 1]) / 2
else:
	quantile_075 = daily_stock_price[math.floor(p)]
print("quantile_075 =", quantile_075)

# 方差
variance = sum_element([(x - daily_average) ** 2 for x in daily_stock_price]) / (f.shape[0] - 1)
print("variance =", variance)

# 标准差
standard_deviation = math.sqrt(variance)
print("standard_deviation =", standard_deviation)

# 变异系数
CV = standard_deviation / daily_average
print("CV =", "%.2f%%" % (CV * 100))

# 极差
Range = daily_stock_price[f.shape[0] - 1] - daily_stock_price[0]
print("Range =", Range)

# 四分位极差
Range_4 = quantile_075 - quantile_025
print("Range_4 =", Range_4)

# 偏度
skewness = (f.shape[0] / ((f.shape[0] - 1) * (f.shape[0] - 2))) * (1 / (standard_deviation ** 3)) * sum_element([(x - daily_average) ** 3 for x in daily_stock_price])
print("skewness =", skewness)

# 峰度
peakedness = ((((f.shape[0] * (f.shape[0] + 1))) / ((f.shape[0] - 1) * (f.shape[0] - 2) * (f.shape[0] - 3))) * (1 / (standard_deviation ** 4)) * sum_element([(x - daily_average) ** 4 for x in daily_stock_price])) - ((3 * (f.shape[0] - 1) ** 2) / ((f.shape[0] - 2) * (f.shape[0] - 3)))
print("peakedness =", peakedness)