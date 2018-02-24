import matplotlib.pyplot as plt
import pandas as pd
import numpy as py

unrate = pd.read_csv("unrate.csv");
unrate['DATE'] = pd.to_datetime(unrate['DATE'], errors='coerce')
unrate['MONTH'] = unrate['DATE'].dt.month

#set 5 charts on a plot
color = ["red", "blue", "green", "orange", "black"]

figure = plt.figure(figsize= (10, 6))
for i in range(0, 5):
    plt.plot(unrate[i * 12 : i * 12 + 12]['MONTH']
             , unrate[i * 12 : i * 12 + 12]['VALUE']
             , c = color[i]
             , label= str(1948 + i))

plt.legend(loc='upper left')
plt.show()

#set 2 line charts on a subplot.
# fig = plt.figure(figsize=(6, 6))
# plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red')
# plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='blue')
#
# plt.show()

#set 5 charts on 5 different subplot
# fig = plt.figure(figsize=(12,12))
#
# for i in range(5):
#     ax = fig.add_subplot(5,1,i+1)
#     start_index = i*12
#     end_index = (i+1)*12
#     subset = unrate[start_index:end_index]
#     ax.plot(subset['DATE'], subset['VALUE'])
#     plt.xticks(rotation=90)
#
# plt.show()