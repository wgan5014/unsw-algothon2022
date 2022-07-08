import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf

nInst=100
currentPos = np.zeros(nInst)

all_instruments = [i for i in range(nInst)]
df = pd.read_csv("./prices.txt", delim_whitespace=True, names=all_instruments)
arr = df[all_instruments]

plot_acf(arr[0], lags=40)

def getMyPosition (prcSoFar):
    global currentPos

    # Build your function body here

    return currentPos