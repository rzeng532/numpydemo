import pandas as pd
import numpy as np

def null_count_col(column):
    return len(column[pd.isnull(column)])

titanic_survival = pd.read_csv('titanic_survival.csv')

age = titanic_survival['age']
print(len(age))

#计算age 列为空的数据
age_nul = pd.isnull(age)
age_null_true = age[age_nul]

#计算age 列非空的数据
age_null_not_true = age[~age_nul]
print(len(age_null_not_true))
correct_mean_age = sum(age_null_not_true) / len(age_null_not_true)
print(correct_mean_age)

age_null_count = len(age_null_true)
print(age_null_count)

#计算mean
passenger_classes = [1, 2, 3]
fares_by_class = {}

for this_class in passenger_classes:
    class_rows = titanic_survival[titanic_survival['pclass'] == this_class]
    fares_by_class[this_class] = class_rows['fare'].mean()

print(fares_by_class)

#通过Pivot tables
#index : group by, 分组依据，如pclass 有1,2,3，则分成3个group，类似于key
#values：用哪列进行运算
#aggfunc:使用的运算方法
passenger_age = titanic_survival.pivot_table(index="pclass", values="age", aggfunc=np.mean)
print(passenger_age)

#通过Pivot tables对多列进行运算
port_stats = titanic_survival.pivot_table(index='embarked', values=['fare', 'survived'], aggfunc=np.sum)
print(port_stats)

#dropna() 刨除空值
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0, subset=['age', 'sex'])

first_ten_rows  = new_titanic_survival.iloc[:10]
row_position_fifth = new_titanic_survival.iloc[:15]
row_index_25 = new_titanic_survival.loc[25]

#对列表的数据进行选择，单个或区域计算
#iloc = int location，下标计算
#loc，label计算
row_index_1100_age = new_titanic_survival.loc[1100, 'age']
row_index_25_survived = new_titanic_survival.loc[25, 'survived']
five_rows_three_cols = new_titanic_survival.iloc[0:5, 0:3]

#重新设置index
#drop=True，不用老的index
titanic_reindexed = new_titanic_survival.reset_index(drop=True)
print(titanic_reindexed.iloc[:5, :3])

#apply 函数
print("column_null_count start")
column_null_count = titanic_survival.apply(null_count_col)
print(column_null_count)

#apply 操作行数据
def minor(row):
    passager_age = row['age']

    if pd.isnull(passager_age):
        return 'unknown'
    elif passager_age < 18:
        return 'minor'
    elif passager_age >= 18:
        return 'adult'

age_labels = titanic_survival.apply(minor, axis = 1)
print(age_labels)

#自由操作
#大人 & 小孩生存数
titanic_survival['age_labels'] = age_labels
#各个年龄段，活下来的个数
age_group_survival = titanic_survival.pivot_table(index='age_labels', values='survived', aggfunc=np.sum)

#各个年龄段，生存率
age_group_survival_per = titanic_survival.pivot_table(index='age_labels', values='survived', aggfunc=np.mean)

print(age_group_survival)
print(age_group_survival_per)

#各个年龄段乘客数目
age_group_survival_count = titanic_survival.pivot_table(index='age_labels', values='survived', aggfunc=np.alen)
print(age_group_survival_count)

#各个年龄段，领便当的人数
print(age_group_survival_count - age_group_survival)

# def how_many_die(row):
#     row_survived = row['survived']
#     if row_survived == 0:
#         return 1
#     else:
#         return 0

# first_ten = titanic_survival.iloc[:, :2]
# print(first_ten)
# print(np.mean(first_ten))



