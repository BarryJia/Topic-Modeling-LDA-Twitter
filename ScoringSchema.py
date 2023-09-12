import pandas as pd
import re
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import  matplotlib
import seaborn as sns

def running(file):
    count = 0
    with open(file+'CollectedData_topics.txt', 'r', encoding='utf-8') as f:
        list = []
        list2 = []
        score = []
        for i in f:
            if (count%2 == 0):
                # list.append(i)
                i = i.strip('\n')
                list.append(i)
                score.append(0)
                # print(list)
            else:
                # list2.append(i)
                i = i.strip('\n')
                list2.append(i)
                # print(list2)
                # break
            count += 1
    # print(list)
    # print(list2)
    # print(score)

    #带有 nCov covid corona disease 的主题分数+1
    covidList = ['covid','nCov','corona','disease']
    for i in range(len(list2)):
        for j in covidList:
            if(j.lower() in list2[i].lower()):
                score[i]+=1


    #带有情绪性词语的主题分数+1 [angry,nervous,distracted,terrified,sad,pensive,afraid,depressed,annoyed,furious,overwhelmed]
    emotionList = ['angry','nervous','distracted','terrified','sad','pensive','afraid','depressed','annoyed','furious','overwhelmed']
    for i in range(len(list2)):
        for j in emotionList:
            if(j in list2[i].lower()):
                score[i]+=1
    for i in range(len(score)):
        if(score[i]>0):
            print('Topic '+str(i)+': '+str(score[i]))


#每出现一次+1
# def running(file):
    df = pd.read_csv(file+'final_new.csv')
    topicList = df['topic_x']
    # newTopList = random.shuffle(topicList)
    randomList = []
    for i in range(10000):
        randomList.append(random.choice(topicList))
    listTotal = []
    print(len(randomList))
    for v in range(100):
        listTotal.append(0)
    for i in randomList:
        for j in range(100):
            if str(i)==str(j):
                listTotal[j] += 1
    print(listTotal)
    totalScore = 0
    for i in range(len(score)):
        if (score[i] > 0):
            totalScore += score[i]*listTotal[i]
    print(totalScore)
    return totalScore

scoreTest = []
scoreTest.append(running('data/TimeSegmentation/Feb/Feb'))
scoreTest.append(running('data/TimeSegmentation/March_1_5/March_1_5_'))
scoreTest.append(running('data/TimeSegmentation/March_6_10/March_6_10_'))
scoreTest.append(running('data/TimeSegmentation/March_11_15/March_11_15_'))
scoreTest.append(running('data/TimeSegmentation/March_16_20/March_16_20_'))
scoreTest.append(running('data/TimeSegmentation/March_21_25/March_21_25_'))
scoreTest.append(running('data/TimeSegmentation/March_26_31/March_26_31_'))
scoreTest.append(running('data/TimeSegmentation/April_1_5/April_1_5_'))
scoreTest.append(running('data/TimeSegmentation/April_6_10/April_6_10_'))
scoreTest.append(running('data/TimeSegmentation/April_11_15/April_11_15_'))
scoreTest.append(running('data/TimeSegmentation/April_16_20/April_16_20_'))
scoreTest.append(running('data/TimeSegmentation/April_21_25/April_21_25_'))
scoreTest.append(running('data/TimeSegmentation/April_26_30/April_26_30_'))
print(len(scoreTest))
print(scoreTest)
sns.set_style("whitegrid")
sns.set_style("darkgrid")
sns.set_style("dark")
sns.set_style("white")
sns.set_style("ticks")
sns.despine(offset=30,left=True)
plt.figure(figsize=(16, 9))
plt.xlabel('Time')
plt.ylabel('Score')
plt.bar(['2/1-2/29','3/1-3/5','3/6-3/10','3/11-3/15','3/16-3/20','3/21-3/25','3/26-3/31','4/1-4/5','4/6-4/10','4/11-4/15','4/16-4/20','4/21-4/25','4/26-4/30'],scoreTest)
plt.xticks(fontsize=8)
plt.title("Total Score of Each Part of Time.")
plt.show()
