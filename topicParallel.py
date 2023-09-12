import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import  matplotlib
import seaborn as sns


#五天一个总的file
#一个file一套topic（100）
#首先将topic file和某一天的合并
#计算每一天的topic总数
#计算方差



# def doIt(file, newfile):
#     print(file)
#     print(newfile)
#     df1 = pd.read_csv(newfile+'.csv')
#     df2 = pd.read_csv(file+'CollectedData_doc_topics.csv')
#     outfile = pd.merge(df1, df2, left_on='tweet_id', right_on='id')
#     outfile = outfile.drop(['created_at', 'user_id', 'geo_source', 'user_location', 'geo', 'place', 'id', 'location'], axis=1)
#     outfile.to_csv(newfile+'final.csv', index=False, encoding='utf-8')
#
#
#     df1 = pd.read_csv(newfile+'final.csv')
#     df2 = pd.read_csv(file+'CollectedData_new.csv')
#     outfile = pd.merge(df1, df2, left_on='tweet_id', right_on='id')
#     outfile = outfile.drop(['fenci', 'id'], axis=1)
#     outfile.to_csv(newfile+'final_new.csv', index=False, encoding='utf-8')
#     print('done')
# file = 'data/TimeSegmentation/Feb/Feb'
# newfile = 'data/new/Feb/0229t1'
# doIt(file,newfile)
# for i in range(2,29):
#     if(i < 10):
#         doIt('data/TimeSegmentation/Feb/Feb', 'data/new/Feb/020'+str(i)+'t1')
#     else:
#         doIt('data/TimeSegmentation/Feb/Feb', 'data/new/Feb/02'+str(i)+'t1')


# def makeList(file):
#     df = pd.read_csv(file)
#     list = df['topic_x']
#     listTotal = []
#     names = []
#     e = []
#     for v in range(100):
#         listTotal.append(0)
#         names.append("Topic " + str(v))
#     for i in list:
#         for j in range(100):
#             if str(i) == str(j):
#                 listTotal[j] += 1
#     print(listTotal)
#     # print(names)
#     return listTotal
# # makeList('data/new/Feb/0201t1final_new.csv')
# topicList = []
# totalList = []
# for i in range(1,30):
#     if(i < 10):
#         topicList.append(makeList('data/new/Feb/020'+str(i)+'t1final_new.csv'))
#     else:
#         topicList.append(makeList('data/new/Feb/02'+str(i)+'t1final_new.csv'))
# print(len(topicList))
# for y in range(100):
#     newlist = []
#     for x in range(29):
#         # for y in range(100):
#         newlist.append(topicList[x][y])
#     totalList.append(newlist)
# print(len(totalList))

# saveList = np.array(totalList)
# np.save('data/TimeSegmentation/Feb/saveList.npy',saveList)

totalList = np.load('data/TimeSegmentation/Feb/saveList.npy')
totalList = totalList.tolist()


# sns.set_style("whitegrid") #横坐标有标线，纵坐标没有标线，背景白色
# sns.set_style("darkgrid") #默认，横纵坐标都有标线，组成一个一个格子，背景稍微深色
# sns.set_style("dark")#背景稍微深色，没有标线线
# sns.set_style("white")#背景白色，没有标线线
# sns.set_style("ticks") #xy轴都有非常短的小刻度
# sns.despine(offset=30,left=True) #去掉上边和右边的轴线，offset=30表示距离轴线（x轴）的距离,left=True表示左边的轴保留
# FebMon = []
# for i in range(1,30):
#     FebMon.append('2.'+str(i))
# for m in range(0,100):
#     plt.figure(figsize=(16, 9))
#     plt.bar(FebMon,totalList[m])
#     plt.plot(totalList[m], sns.xkcd_rgb["pale red"])
#     plt.title("Trends of Topic "+str(m)+" in Feb.")
#     plt.savefig('data/TimeSegmentation/Feb/Topic_'+str(m)+'.png')
#     # plt.show()

variance = []
standardDeviation = []
for m in range(0,100):
    arr_var = np.var(totalList[m])
    arr_std = np.std(totalList[m], ddof=1)
    variance.append(arr_var)
    standardDeviation.append(arr_std)
print(variance)
print(standardDeviation)
sns.set_style("whitegrid") #横坐标有标线，纵坐标没有标线，背景白色
sns.set_style("darkgrid") #默认，横纵坐标都有标线，组成一个一个格子，背景稍微深色
sns.set_style("dark")#背景稍微深色，没有标线线
sns.set_style("white")#背景白色，没有标线线
sns.set_style("ticks") #xy轴都有非常短的小刻度
sns.despine(offset=30,left=True) #去掉上边和右边的轴线，offset=30表示距离轴线（x轴）的距离,left=True表示左边的轴保留
TopicName = []
for i in range(0,100):
    TopicName.append(str(i))
plt.figure(figsize=(16, 9))
plt.bar(TopicName,standardDeviation)
plt.xticks(fontsize=8)
# plt.plot(variance, sns.xkcd_rgb["pale red"])
plt.title("Standard Deviation of Topics in Feb.")
plt.show()

# plt.savefig('data/TimeSegmentation/Feb/Topic_'+str(m)+'.png')
