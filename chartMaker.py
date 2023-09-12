import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sns.set_style("whitegrid") #横坐标有标线，纵坐标没有标线，背景白色
sns.set_style("darkgrid") #默认，横纵坐标都有标线，组成一个一个格子，背景稍微深色
sns.set_style("dark")#背景稍微深色，没有标线线
sns.set_style("white")#背景白色，没有标线线
sns.set_style("ticks") #xy轴都有非常短的小刻度
sns.despine(offset=30,left=True) #去掉上边和右边的轴线，offset=30表示距离轴线（x轴）的距离,left=True表示左边的轴保留

# plt.plot([1, 2, 3, 5, 2, 1])
# plt.show()


listCount = []
listDate = []
def getTotalNumber(months, days):
# days = 30
# months = 2
    for i in range(days):
        count = 0
        if 0< i < 10:
            # with open('data/after/0'+str(months)+'0'+str(i)+'t1.csv', 'r') as f:
            #     for j in f.readline():
            #         count+=1
            df = pd.read_csv('data/new/0'+str(months)+'0'+str(i)+'t1.csv')
            listCount.append(len(df))
            if i % 3 == 0 or i == 1:
                listDate.append("0"+str(months)+"0"+str(i))
            else:
                listDate.append(" "*int(str(months)+"0"+str(i)))
        elif i >= 10:
            # with open('data/after/0' + str(months) + str(i) + 't1.csv', 'r') as f:
            #     for j in f.readline():
            #         count+=1
            df = pd.read_csv('data/new/0' + str(months) + str(i) + 't1.csv')
            listCount.append(len(df))
            if i % 3 == 0 or i == 1:
                listDate.append("0" + str(months) + str(i))
            else:
                listDate.append(" "*int(str(months)+str(i)))
getTotalNumber(2, 30)
getTotalNumber(3, 32)
getTotalNumber(4, 31)
print(listCount)
print(len(listCount))
plt.figure(figsize=(100,100), dpi= 80)
plt.bar(listDate, listCount)
plt.plot(listCount, sns.xkcd_rgb["pale red"])
plt.title("Total Tweets Amount in 4 Countries between Feb. to Apr.")
plt.show()
