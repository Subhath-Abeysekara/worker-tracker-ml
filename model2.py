import pandas as pd
import numpy as np
import pickle

df1 = pd.read_csv('/Users/DFT/Downloads/ratings_Beauty.csv')
df2 = df1.head(50)
print(df2)


def func1(m):
    options = {m}
    df3 = df2[df2['Rating'].isin(options)]
    #df4 = df3['PrjecttId'].value_counts()
    df4 = df3.groupby(['PrjecttId'])['Rating'].count().reset_index(
        name='Count').sort_values(['Count'], ascending=False)
    print(df4.head(5))
    return df4.head(5)

func1(5)
