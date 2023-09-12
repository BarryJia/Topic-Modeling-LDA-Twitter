# import seaborn as sns
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def running(file, path):
    sns.set_style("whitegrid") #横坐标有标线，纵坐标没有标线，背景白色
    sns.set_style("darkgrid") #默认，横纵坐标都有标线，组成一个一个格子，背景稍微深色
    sns.set_style("dark")#背景稍微深色，没有标线线
    sns.set_style("white")#背景白色，没有标线线
    sns.set_style("ticks") #xy轴都有非常短的小刻度
    sns.despine(offset=30,left=True) #去掉上边和右边的轴线，offset=30表示距离轴线（x轴）的距离,left=True表示左边的轴保留

    # plt.plot(np.arange(10))
    # plt.show()
    x = [1, 2, 3, 4]
    explode = (0.05, 0, 0, 0)
    labels = ['one', 'two', 'three', 'four']
    # explode = ['one', 'two', 'three', 'four', 'five']
    # explode = []
    # plt.pie(x, explode = explode, labels = labels, shadow=True,pctdistance=0.6,labeldistance=1.1, autopct='%2.0f%%', startangle=90) # explode表示部分扇形突出，x,label,explode均为数组形式数据
    # plt.show()
    df = pd.read_csv(file)
    list = df['topic_x']
    listTotal = []
    names = []
    e = []
    for v in range(100):
        listTotal.append(0)
        names.append("Topic "+str(v))
    for i in list:
        for j in range(100):
            if str(i)==str(j):
                listTotal[j] += 1
    print(listTotal)
    print(names)
    topTenList = sorted(listTotal,reverse=True)[:10]  # reverse是为了降序排列
    print(topTenList)
    # for i in listTotal:
    #     if(len(topTenList) <= 10):
    newlist = []
    newnames = []
    others = 0
    for i in range(len(listTotal)):
        if listTotal[i] >= topTenList[9]:
            newlist.append(listTotal[i])
            newnames.append(names[i])
            e.append(0)
        # else:
        #     others += listTotal[i]
    # newnames.append("Others")
    # newlist.append(others)
    # e.append(0)
    max_index = newlist.index(max(newlist, key=abs))
    e[max_index] = 0.05
    print(newlist)
    print(newnames)
    plt.figure(figsize=(16, 9))
    plt.pie(newlist, labels=newnames, explode = e, shadow=False,pctdistance=0.6,labeldistance=1.1, autopct='%2.0f%%', startangle=90)
    plt.title("The Proportion of Top 10 Topic Distribution")
    plt.legend(loc='lower right', bbox_to_anchor=(1.5, -0.1))
    plt.grid()
    # plt.figure(figsize=(16, 9))
    plt.savefig(path+'.png')
    print('finish: '+file)
    # plt.show()
# total = 0
# for i in listTotal:
#     total += i
# print(total)

running('data/TimeSegmentation/March_11_15/March_11_15_final_new.csv','data/TimeSegmentation/March_11_15/March_11_15_topTen')
running('data/TimeSegmentation/April_1_5/April_1_5_final_new.csv','data/TimeSegmentation/April_1_5/April_1_5_topTen')
running('data/TimeSegmentation/April_6_10/April_6_10_final_new.csv','data/TimeSegmentation/April_6_10/April_6_10_topTen')
running('data/TimeSegmentation/April_11_15/April_11_15_final_new.csv','data/TimeSegmentation/April_11_15/April_11_15_topTen')
running('data/TimeSegmentation/April_16_20/April_16_20_final_new.csv','data/TimeSegmentation/April_16_20/April_16_20_topTen')
running('data/TimeSegmentation/April_21_25/April_21_25_final_new.csv','data/TimeSegmentation/April_21_25/April_21_25_topTen')
running('data/TimeSegmentation/April_26_30/April_26_30_final_new.csv','data/TimeSegmentation/April_26_30/April_26_30_topTen')