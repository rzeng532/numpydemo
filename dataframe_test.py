import pandas as pd
import numpy as np

fandango = pd.read_csv("fandango_score_comparison.csv")

#print(fandango.head(2))

f_index = fandango.index

#print(f_index)
shape = fandango.shape
print(shape[0])

#select - iloc[]
first_last = fandango.iloc[[0, shape[0] - 1]]

#set index,
# inplace: If set to True, this parameter will set the index for the current, "live" dataframe, instead of returning a new dataframe
# drop: If set to False, this parameter will keep the column we specified as the index, instead of dropping it.
fandango_films = fandango.set_index('FILM', drop=False)
#print(fandango_films.index)

#select - loc[]
best_movies_ever = fandango_films.loc[["The Lazarus Effect (2015)", "Gett: The Trial of Viviane Amsalem (2015)", "Mr. Holmes (2015)"]]

#apply & lambda
#找出使用float类型打分的评分网站和机构 -> 在电影dataframe中将这些机构的打分都 double 一下。
types = fandango_films.dtypes
#print("Step 1")
#print(types[0:4])
float_film = types[types.values == 'float64'].index
#print("Step 2")
#print(float_film[0:4])
float_df = fandango_films[float_film]
#print("Step 3")
#print(float_df[0:4])

halved_df = float_df.apply(lambda x : x / 2)

#apply for index by axis, default is 0 - column
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_means = rt_mt_user.apply(lambda x : np.mean(x), axis = 1)
print(rt_mt_means[0:5])