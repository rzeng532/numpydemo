import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10, 4), columns=list("abcd"))
print(df)

df['a'].hist(bins=100)
plt.show()