import pandas as pd
data = pd.read_csv("000001.csv",sep=',')
daily = (data['high']+data['low'])/2

cv = daily.mean()/daily.std()
four_point_range = daily.quantile(.75)-daily.quantile(.25)
print("均值: %f" %daily.mean())
print("中位数: %f" %daily.median())
print("0.25分位数: %f" %daily.quantile(.25))
print("0.75分位数: %f" %daily.quantile(.75))
print("方差: %f" %daily.var())
print("标准差: %f" %daily.std())
print("变异系数: %f" %cv)
print("极差: %f" %daily.ptp())
print("四分位极差: %f" %four_point_range)
print("偏度: %f" %daily.skew())
print("峰度: %f" %daily.kurt())