import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv('train.csv')

#两种获取方式，哪种效率更高？
titanic = titanic[["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
# titanic = titanic.loc[:, ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]

titanic = titanic.dropna()

#直方图
# sns.distplot(titanic["Fare"])
# plt.show()

#带面积的趋势图，shade = True为显示阴影，False时不显示阴影
# sns.kdeplot(titanic["Age"], shade=True)
# plt.xlabel('Age')
# plt.show()

#Note：该设置需要在设置data前使用。设置背景图
# sns.set_style('dark')
# sns.kdeplot(titanic['Age'], shade = True)
#设置边框，True表示隐藏
#Note：该设置需要在设置数据之后使用
# sns.despine(left=True, bottom = True)
#
# plt.xlabel('Age')
# plt.show()

#sns.FacetGrid
# g = sns.FacetGrid(titanic, col="Survived", size=6, row="Pclass")
# g.map(sns.kdeplot, "Age", shade=True)
#
# sns.despine(left=True, bottom = True)
# plt.show()

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue="Sex", size=3)
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)
#plt.legend(loc='upper right')
plt.show()