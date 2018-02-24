import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

#画一条线：
#ax = women_degrees.plot(x='Year', y='Biology')
#Or:
#plt.plot(women_degrees['Year'], women_degrees['Biology'])
#plt.show()

#画多条线：
#画布快要可不要
#fig = plt.figure(figsize=(6, 6))

# plt.plot(women_degrees['Year'], women_degrees['Biology'], c='blue', label='Women')
# plt.plot(women_degrees['Year'], 100 - women_degrees['Biology'], c='green', label="Men")
# plt.title('Percentage of Biology Degrees Awarded By Gender')
# plt.legend(loc='upper left')
#
# plt.show()

# fig, ax = plt.subplots()
#
# ax.plot(women_degrees['Year'], women_degrees['Biology'], c='blue', label='Women')
# ax.plot(women_degrees['Year'], 100 - women_degrees['Biology'], c='green', label="Men")
#tick_params 作用？
# ax.tick_params(bottom='off', top="off", left="off", right="off")
#去掉4条边
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
#
# ax.set_title('Percentage of Biology Degrees Awarded By Gender')
# ax.legend(loc="upper right")
#
# plt.show()

#建一个4 x 4的图
# fig = plt.figure(figsize=(12, 12))
#
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)
# ax4 = fig.add_subplot(2,2,4)
#
# ax1.plot(women_degrees['Year'], women_degrees['Biology'], c='blue', label='Women')
# ax1.plot(women_degrees['Year'], 100 - women_degrees['Biology'], c='green', label="Men")
# ax1.set_title('Biology')
# ax1.set_ylim(0, 100)
# ax1.set_xlim(1968 , 2011)
# ax1.tick_params(bottom="off", top="off", left="off", right="off")
# ax1.spines['right'].set_visible(False)
# ax1.spines['left'].set_visible(False)
# ax1.spines['top'].set_visible(False)
# ax1.spines['bottom'].set_visible(False)
#
# ax2.plot(women_degrees['Year'], women_degrees['Computer Science'], c='blue', label='Women')
# ax2.plot(women_degrees['Year'], 100 - women_degrees['Computer Science'], c='green', label="Men")
# ax2.set_title('Computer Science')
# ax2.set_ylim(0, 100)
# ax2.set_xlim(1968 , 2011)
# ax2.tick_params(bottom="off", top="off", left="off", right="off")
# ax2.spines['right'].set_visible(False)
# ax2.spines['left'].set_visible(False)
# ax2.spines['top'].set_visible(False)
# ax2.spines['bottom'].set_visible(False)
#
# ax3.plot(women_degrees['Year'], women_degrees['Engineering'], c='blue', label='Women')
# ax3.plot(women_degrees['Year'], 100 - women_degrees['Engineering'], c='green', label="Men")
# ax3.set_title('Engineering')
# ax3.set_ylim(0, 100)
# ax3.set_xlim(1968 , 2011)
# ax3.tick_params(bottom="off", top="off", left="off", right="off")
# ax3.spines['right'].set_visible(False)
# ax3.spines['left'].set_visible(False)
# ax3.spines['top'].set_visible(False)
# ax3.spines['bottom'].set_visible(False)
#
# ax4.plot(women_degrees['Year'], women_degrees['Math and Statistics'], c='blue', label='Women')
# ax4.plot(women_degrees['Year'], 100 - women_degrees['Math and Statistics'], c='green', label="Men")
# ax4.set_title('Math and Statistics')
# ax4.legend(loc = 'upper right')
# ax4.set_ylim(0, 100)
# ax4.set_xlim(1968 , 2011)
# ax4.spines['right'].set_visible(False)
# ax4.spines['left'].set_visible(False)
# ax4.spines['top'].set_visible(False)
# ax4.spines['bottom'].set_visible(False)
# ax4.tick_params(bottom="off", top="off", left="off", right="off")
#
# plt.show()

#另外一种实现方式：
# major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
# fig = plt.figure(figsize=(12, 12))
#
# for sp in range(0,4):
#     ax = fig.add_subplot(2,2,sp+1)
#     ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
#     ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
#     # Add your code here.
#
# # Calling pyplot.legend() here will add the legend to the last subplot that was created.
# plt.legend(loc='upper right')
# plt.show()
# major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
# fig = plt.figure(figsize=(12, 12))
#
# for sp in range(0,4):
#     ax = fig.add_subplot(2,2,sp+1)
#     ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
#     ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
#     for key,spine in ax.spines.items():
#         spine.set_visible(False)
#     ax.set_xlim(1968, 2011)
#     ax.set_ylim(0,100)
#     ax.set_title(major_cats[sp])
#     ax.tick_params(bottom="off", top="off", left="off", right="off")
#
# # Calling pyplot.legend() here will add the legend to the last subplot that was created.
# plt.legend(loc='upper right')
# plt.show()

#一行
# fig = plt.figure(figsize=(18, 3))
# stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
# for sp in range(0,6):
#     ax = fig.add_subplot(1,6,sp+1)
#     ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=(0/255,107/255,164/255), label='Women', linewidth=3)
#     ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=(255/255,128/255,14/255), label='Men', linewidth=3)
#     for key,spine in ax.spines.items():
#         spine.set_visible(False)
#     ax.set_xlim(1968, 2011)
#     ax.set_ylim(0,100)
#     ax.set_title(stem_cats[sp])
#     if sp == 0:
#         ax.text(2005, 87, "Men")
#         ax.text(2002, 8, "Women")
#     elif sp == 5:
#         ax.text(2005, 62, "Men")
#         ax.text(2001, 35, "Women")
#     ax.tick_params(bottom="off", top="off", left="off", right="off")
# plt.legend(loc='upper right')
# plt.show()

#Jupter tasks
women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0 / 255, 107 / 255, 164 / 255)
cb_orange = (255 / 255, 128 / 255, 14 / 255)

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering', 'Computer Science']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

#As row data
row_data = [stem_cats, lib_arts_cats, other_cats]

fig = plt.figure(figsize=(9, 21))

for col_index in range(0, 3):
    row_data_cats = row_data[col_index]
    for sp in range(0, len(row_data_cats)):
        ax = fig.add_subplot(7, 3, sp * 3 + col_index + 1)
        ax.plot(women_degrees['Year'], women_degrees[row_data_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
        ax.plot(women_degrees['Year'], 100 - women_degrees[row_data_cats[sp]], c=cb_orange, label='Men', linewidth=3)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.set_xlim(1968, 2011)
        ax.set_ylim(0, 100)
        #设置y轴可显示的刻度，list
        ax.set_yticks([0, 100])
        ax.axhline(50, c=(171 / 255, 171 / 255, 171 / 255), alpha=0.3)
        ax.set_title(stem_cats[sp])
        #labelbottom='on'
        ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')

        if sp == 0:
            ax.text(2005, 87, 'Men')
            ax.text(2002, 8, 'Women')
        elif sp == len(row_data_cats) - 1:
            ax.text(2005, 62, 'Men')
            ax.text(2001, 35, 'Women')

#saving result picture
plt.savefig('gender_degrees.png')
plt.show()