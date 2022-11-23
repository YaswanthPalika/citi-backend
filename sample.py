import seaborn as sb
from scipy.stats import pearsonr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('citi.csv')
data.head(11)
data.shape
symbols = data['Symbol'].unique()
Symbol_dict = {key: [] for key in symbols}
for i in range(len(data)):
    Symbol_dict[data.loc[i, 'Symbol']].append(data.loc[i, 'CLOSE'])
len(Symbol_dict['Gold'])
moving_averages_1Day = {key: [] for key in symbols}
for key in Symbol_dict:
    print(key)
for key in Symbol_dict:
    i = 1
    cum_sum = np.cumsum(Symbol_dict[key])
    while i <= 163:
        window_average = round(cum_sum[i-1] / i, 2)
        moving_averages_1Day[key].append(window_average)
        i = i+1

for key in moving_averages_1Day:
    print(len(moving_averages_1Day[key]))

# correlation
corr, _ = pearsonr(
    moving_averages_1Day['Gold'], moving_averages_1Day['Silver'])
print('Pearsons correlation: %.3f' % corr)
d = pd.DataFrame.from_dict(moving_averages_1Day)
dataplot = sb.heatmap(d.corr(), annot=True)
correlation = d.corr()
corr_pairs = {}
a = []
i = 1
for x in correlation:
    for j in range(i, len(correlation[x])):
        if correlation[x][j] <= -0.5 or correlation[x][j] >= 0.5:
            key = x+" vs "+symbols[j]
        # print(key)
            corr_pairs[key] = correlation[x][j]
       # print(correlation[x][j])
    i = i+1

Keymax = max(zip(corr_pairs.values(), corr_pairs.keys()))[1]
Keymax = min(zip(corr_pairs.values(), corr_pairs.keys()))[1]
