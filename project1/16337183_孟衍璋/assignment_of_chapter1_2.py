import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math
from scipy import stats

f = pd.read_csv("000006.csv")

# 每日股价 = （每日最低价+每日最高价）/ 2
daily_stock_price = ((f.high + f.low) / 2).tolist()

daily_stock_price_sorted = sorted(daily_stock_price)

# 画出价格-频率直方图
plt.subplot(221)
plt.hist(np.array(daily_stock_price_sorted), bins = np.linspace(daily_stock_price_sorted[0], daily_stock_price_sorted[f.shape[0] - 1], int(math.sqrt(f.shape[0]))), density = 1, rwidth=0.8)
plt.title("price-frequency histogram")

# 画出正态QQ图
plt.subplot(222)
stats.probplot(daily_stock_price_sorted, dist = "norm", plot = plt)
plt.title("q-q plot")

# 画出差值的直方图
difference = list()
for i in range(f.shape[0] - 1):
	difference.append(daily_stock_price[i + 1] - daily_stock_price[i])
difference.sort()

plt.subplot(223)
plt.hist(np.array(difference), bins = np.linspace(difference[0], difference[len(difference) - 1], int(math.sqrt(len(difference)))), density = 1, rwidth = 0.8)
plt.title("difference histogram")

# 画出差值的正态QQ图
plt.subplot(224)
stats.probplot(difference, dist = "norm", plot = plt)
plt.title("q-q plot")

plt.show()