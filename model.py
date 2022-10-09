import pandas as pd
import numpy as np
import pickle

x = pd.read_csv('/Users/DFT/ings_Beauty.csv')
#print(x)
df1=pd.read_csv('/Users/DFT/Downloads/tmdb_5000_credits.csv/tmdb_5000_credits.csv')
df2=pd.read_csv('/Users/DFT/Downloads/tmdb_5000_movies.csv')

df1.columns = ['id','tittle','cast','crew']
df2= df2.merge(df1,on='id')

#get first 50 data to analyze
df2 = df2.head(50)
print(df2)
C= df2['vote_average'].mean()
print(C)

m= df2['vote_count'].quantile(0.9)
print(m)

q_projct = df2.copy().loc[df2['vote_count'] >= m]
print(q_projct.shape)


def func(q_projct=q_projct):


    def weighted_rating(x,  m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        # Calculation based on the IMDB formula
        return ((v / (v + m) * R) + (m / (m + v) * C))

    # Define a new feature 'score' and calculate its value with `weighted_rating()`
    q_projct['score'] = q_projct.apply(weighted_rating, axis=1)

    # Sort movies based on score calculated above
    q_projct = q_projct.sort_values('score', ascending=False)

    # Print the top 15 movies
    # print(#Sort movies based on score calculated above
    #
    # #Print the top 15 movies
    # q_projct[['title', 'vote_count', 'vote_average', 'score']].head(5))

    best_projects = q_projct[['title', 'vote_count', 'vote_average', 'score']].head(10)

    print(best_projects)

    return best_projects

func()


