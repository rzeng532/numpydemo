import pandas as pd

import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix

recent_grads = pd.read_csv('recent-grads.csv')

# print(recent_grads.head())
# print(recent_grads.tail())

#填充 NaN项
raw_data_count = recent_grads.shape[0]
print("Row num: %d" % raw_data_count)

# recent_grads.fillna(value=None, axis=0)
recent_grads_new = recent_grads.dropna(axis=0, how='any')
row_data_count_new = recent_grads_new.shape[0]
print("New row num: %d" % row_data_count_new)

#使用pandas自动的plot，实现数据展示，只需要填入x & y列即可
# ax = recent_grads.plot(x='Sample_size', y='Employed', kind='scatter')
# ax.set_title('Employed vs. Sample_size')
#
# ax2 = recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')
# ax2.set_title('Unemployment_rate vs. Sample_size')
#
# ax3 = recent_grads.plot(x='Full_time', y='Median', kind='scatter')
# ax3.set_title('Median vs. Full_time')
#
# ax4 = recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')
# ax4.set_title('Unemployment_rate vs. ShareWomen')
#
# ax5 = recent_grads.plot(x='Men', y='Median', kind='scatter')
# ax5.set_title('Median vs. Men')
#
# ax5 = recent_grads.plot(x='Women', y='Median', kind='scatter')
# ax5.set_title('Median vs. Women')
#
# plt.show()

#使用pandas自带的hist图
# ax = recent_grads['Men'].hist(bins=100)
# plt.show()

# ax = recent_grads.plot(x='Men', y='Median', kind='scatter')
# ax2 = recent_grads.plot(x='Women', y='Median', kind='scatter')
# plt.show()

#使用scatter_matrix, scatter & hist 共同显示
scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(10,10))
scatter_matrix(recent_grads[['Sample_size', 'Median', "Unemployment_rate"]], figsize=(10,10))
plt.show()

#柱状图

# new_recent = recent_grads.sort_values("Median")
# new_recent.head(10).plot.bar(x='Major', y='Women')
# print(recent_grads.loc[:, ['Major', 'Median']].head(10))
# new_recent.tail(10).plot.bar(x='Major', y='Women')
# plt.show()
# print(recent_grads.tail(10)['Major', 'Women'])
# print(recent_grads.loc[:5, ['Major', 'Women']])
