import pandas as pd
import scipy.stats as stats

data = pd.read_csv ("000012.csv", sep=',')
data['daily_price'] = (data['high'] + data['low']) / 2

pearson, pp = stats.pearsonr (data['volume'], data['daily_price'])
spearson, sp = stats.spearmanr (data['volume'], data['daily_price'])

print (pearson)
print (spearson)
