import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

conn = sqlite3.connect("factbook.db")

query = "select population,population_growth,birth_rate,death_rate from facts"
result = pd.read_sql_query(query, conn)

cols = ['population', 'population_growth', 'birth_rate', 'death_rate']
#result.plot(result, columns=cols, kind='hist', layout=(2,2))

#result.plot(result['population'], kind='hist')
result.hist()
plt.show()
