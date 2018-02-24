import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df)

first_3 = df.index[:3]
print(first_3)
print(type(first_3))

first_3_A = df['A'][:3]
print(first_3_A)

#select a value:
print(df.loc[df.index[1], 'A'])

# plt.plot([0,1,2], first_3_A)
# plt.xticks(rotation=90)
# plt.show()
#

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()
