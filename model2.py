import pandas as pd
import numpy as np
import pickle

#read the dataset
df1 = pd.read_csv('/Users/DFT/Downloads/ratings_Beauty.csv')
#get first 50 rows
df2 = df1.head(50)
print(df2)


def func1(m):
    #make parameter object
    options = {m}
    #filter data rows acording to rating
    df3 = df2[df2['Rating'].isin(options)]
    #Sort project ids acording to freaquence
    df4 = df3.groupby(['PrjecttId'])['Rating'].count().reset_index(
        name='Count').sort_values(['Count'], ascending=False)
    print(df4.head(5))
    #return first five projects
    return df4.head(5)

func1(5)
