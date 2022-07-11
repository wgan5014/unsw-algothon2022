import pandas as pd
import numpy as np

df = pd.read_csv("prices.txt", delim_whitespace=True, header=None)

import statsmodels.api as sm

ls = []

for i in df:
    for j in df:
        if i == j:
            continue
        
        pct_change_1 = df[i].pct_change()[1:]
        pct_change_2 = df[j].pct_change()[1:]
        
        ccf = sm.tsa.stattools.ccf(pct_change_1, pct_change_2, adjusted=False, )

        val = max(ccf)
        index = np.argmax(ccf)

        ls.append((val, index, i, j))

ls.sort(key=lambda a: a[0])
print(ls[-100:])