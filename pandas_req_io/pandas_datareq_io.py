import pandas as pd
import numpy as np

#In this mission, we learned how to transform columns,
#normalize columns, and use the arithmetic operators to create new columns

#读取csv文件
food_info = pd.read_csv('food_info.csv')

#获取行 & 列信息
col_names = food_info.columns.tolist()
index_names = food_info.index.tolist()
#print(col_names)
# print(index_names)

# print(food_info.loc[:2])
# print(food_info.head(3))

#operation for column values
sodium_grams = food_info['Sodium_(mg)'] / 1000
sugar_milligrams = food_info['Sugar_Tot_(g)'] * 1000
# print(sodium_grams)

#不同列做运算
grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] * food_info["Water_(g)"]
milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] * food_info["Iron_(mg)"]
print(grams_of_protein_per_gram_of_water)

weighted_protein = 2 * food_info['Protein_(g)']
weighted_fat = -0.75 * food_info['Lipid_Tot_(g)']
initial_rating = weighted_protein + weighted_fat

print(initial_rating)

#标准化：new_value = (value_list - min(value_list)) / max(value_list)
max_protein = food_info["Protein_(g)"].max()
normalized_protein = food_info["Protein_(g)"] / max_protein

#新增一列
food_info['Normalized_Protein'] = normalized_protein

#针对某一列数据排序，inplace为true表示在原来的数据中处理而不是返回一个新的数据；
#ascending 某人为True
food_info.sort_values("Norm_Nutr_Index", inplace=True, ascending=False)


