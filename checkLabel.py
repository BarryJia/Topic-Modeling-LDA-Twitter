import csv
import glob


if __name__ == '__main__':
    count = 0
    with open('data/combine/totallyCollectedData_old.csv', 'r', encoding='utf-8') as csvfile:
        readfile = csv.reader(csvfile)
        list = []
        list2 = []
        for i in readfile:
            if (count == 0):
                # list.append(i)
                print(i)
            elif(count == 1):
                # list2.append(i)
                print(i)
                break
            count += 1
    # print(list[0][2])
    # print(list[0][5])
    # print(list2[0][2])
    # print(list2[0][5])
    # count = 0
    # with open('data/TimeSegmentation/March_16_20/March_16_20_wordCloud.txt','a') as f:
    #     with open('data/TimeSegmentation/March_16_20/March_16_20_final_new.csv', 'r', encoding='utf-8') as csvfile:
    #         readfile = csv.reader(csvfile)
    #         list = []
    #         list2 = []
    #         for i in readfile:
    #             if (count == 0):
    #                 # list.append(i)
    #                 print(i)
    #             else:
    #                 f.write(i[3]+' ')
    #                 # list2.append(i)
    #                 # print(i[3])
    #             count += 1