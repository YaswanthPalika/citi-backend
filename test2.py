#import seaborn as sb
from scipy.stats import pearsonr
import sys
import json
import pandas as pd
import numpy as np
x = sys.argv[1]
print("working this")
y = json.loads(x)

data = pd.DataFrame.from_dict(y)

symbols = data['Symbol'].unique()
Symbol_dict = {key: [] for key in symbols}
for i in range(len(data)):
    Symbol_dict[data.loc[i, 'Symbol']].append(data.loc[i, 'CLOSE'])

moving_averages_1Day = {key: [] for key in symbols}

for key in Symbol_dict:
    i = 1
    cum_sum = np.cumsum(Symbol_dict[key])
    while i <= 163:
        window_average = round(cum_sum[i-1] / i, 2)
        moving_averages_1Day[key].append(window_average)
        i = i+1

corr, _ = pearsonr(
    moving_averages_1Day['Gold'], moving_averages_1Day['Silver'])

d = pd.DataFrame.from_dict(moving_averages_1Day)
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
