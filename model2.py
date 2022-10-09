import pandas as pd
import numpy as np
import pickle

df1 = pd.read_csv('/Users/DFT/Downloads/ratings_Beauty.csv')
df2 = df1.head(50)
print(df2)


def func1(m):
    options = {m}
    df3 = df2[df2['Rating'].isin(options)]

    df3['count'] = df3.groupby('PrjecttId')['PrjecttId'].transform(pd.Series.value_counts)
    df3.sort_values('count', ascending=False)
    print(df3)
func1(5)