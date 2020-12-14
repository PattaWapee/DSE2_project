# This script is to get the stock data

import starfishX as sx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


def list_set100():
    return sx.getMemberOfIndex(sx.indexMarket.SET100).values.ravel()


def finance_ratio_df(list_stock):
    all_stock = []
    for stock in list_stock:
        print('Get finance ratio ', stock)
        df = sx.getFinanceRatio(stock)
        if isinstance(df, pd.DataFrame):
            df20 = df.iloc[:, [0]].transpose()
            df20.index = [stock]
            all_stock.append(df20)
    return pd.concat(all_stock)


if __name__ == "__main__":
    set100 = list_set100()
    dat = finance_ratio_df(set100)
    print(dat.head())
