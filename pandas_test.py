import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8])
print(s)

dates = pd.date_range('20130101', periods=6)
print(dates)

#Create
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
print(df.dtypes)

print(df.index)
print(df.columns)
print(df.values)
print(df.describe())
print(df.T)
print(df.sort_index(axis=0, ascending=False))
print(df.sort_values(by='B', ascending=False))

#Select
print("Select start")
print(df.A)
print(df['A'])
print(df.loc['2013-01-01' : '2013-01-04', ['A', 'B']])
print(df.loc['2013-01-01', ['A']])

print(df.iloc[3])



#bool index
# print(df[df.A > 0])
# print(df[((df.A > 0) | (df.B > 0))])
# print(df[df > 0])
print(df)
df['E'] = ['A', 'B', 'C', 'D', 'E', 'E']
print(df[df['E'].isin(['E', 'E'])])

df.at[dates[0],'A'] = 0
print(df)


print("Length of df: %d" % len(df))

# refresh NaN
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['F'])
df1.loc[dates[0]:dates[1],'F'] = 1

print(df1)

# print(df1.dropna(how = 'any'))
# print(df1.dropna(axis=0, how = 'any'))
print(df1.dropna(axis=0, how = 'any', thresh=6))
print(df1.fillna(method='ffill'))


print(pd.isna(df1))
# print(df1.isna)


#Apply method
print(df.apply(np.cumsum))

s = pd.Series(np.random.randint(0, 7, size=10))

print(s)
print(s.value_counts())
print(len(s.value_counts()))
print(s.value_counts())


#Merge
df = pd.DataFrame(np.random.randn(10, 4))
print(df)

pieces = [df[:3], df[4:7], df[8:]]

df1 = pd.concat(pieces)
print(df1)

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'new-bar'], 'rval': [4, 5]})

all = pd.merge(left, right, on='key')
print(all)

df = pd.DataFrame(np.random.randn(4, 4), columns=['A','B','C','D'])
r3 = df.iloc[3]
print(df.append(r3, ignore_index=False))

#Group
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})

print(df.groupby(['A', 'B']).sum())

#resharp
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print(index)
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print(df)