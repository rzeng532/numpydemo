import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#init
reviews = pd.read_csv("fandango_scores.csv")

fig, ax = plt.subplots()

col_x = reviews['Fandango_Ratingvalue']
col_y = reviews['RT_user_norm']

ax.scatter(col_x, col_y, c = 'red')

ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')

plt.show()