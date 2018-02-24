import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#init
reviews = pd.read_csv("fandango_scores.csv")
norm_reviews = reviews[['FILM','RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']]

#create bar plot
fig, ax = plt.subplots()

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_positions = np.arange(5) + 0.75
bar_heights = norm_reviews[num_cols].iloc[0].values

#位置（0.75为偏移量），数值，柱型的宽度
#vertical
# ax.bar(bar_positions, bar_heights, 0.5)
#horizon
ax.barh(bar_positions, bar_heights, 0.5)

#设置X轴每个tick的标签，旋转角度
#ax.set_xticklabels(num_cols, rotation=90)
ax.set_yticklabels(num_cols)

#设置X轴label显示的位置，一般从 1 开始
#如果是0开始，则从（0,0）开始标识
tick_positions = range(1,6)
# ax.set_xticks(tick_positions)
ax.set_yticks(tick_positions)

#设置图标的X,Y标签及图标的title
ax.set_xlabel('Rating Source')
ax.set_ylabel('Average Rating')
ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')

plt.show()