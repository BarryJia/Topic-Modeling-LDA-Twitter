import csv

import pandas as pd


file = "data/combine/totallyCollectedData_small"
# df = pd.read_csv('0208.csv', header = None, names = ['id', 'text', 'text2', 'text3', 'text4', 'fenci'])
# df.to_csv('0208.csv', index = False)
# df = pd.read_csv('0208.csv')
# df['total'] = df['text'].map(str) + df['text2'].map(str)
# df.to_csv('0208new.csv', index = False)
# f = open('0208.csv', 'r', encoding='utf-8')
# f2 = open('0208new.csv', 'w', encoding='utf-8')
count = 0
total = 0
with open(file+'.csv', 'r', encoding='utf-8') as f3:
    csv_reader = csv.reader(f3)
    for row in csv_reader:
        total += 1
        # print(row)
# print(total)
# i = 0
# while True:
#     data = f.readline()
#     mydata = data.split(',')
#     # count += 1
#     if not data:
#         count += 1
#     else:
#     # if count > total:
#     #     f.close()
#     #     f2.close()
#     #     break
#         if (''.join(mydata[0]).isdigit()):
#             f2.write(''.join(mydata[0])+','+''.join(mydata[1:]))
#     if count == 10:
#     # if count == 2*total:
#         print(count)
#         break
# readers = csv.reader(f)

# for i in f:
#     count += 1
# for i in f:
#     data = f.readline()
#     # print(data)
#     mydata = data.split(',')
    # print(mydata)
    # count += 1
    # if (''.join(mydata[0]).isdigit()):
    #         f2.write(''.join(mydata[0])+','+''.join(mydata[1:]))
    # else:
    #     count += 1
        # print(data)
with open(file+'_new.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    with open(file+'.csv', 'r', encoding='utf-8') as f4:
        csv_reader_new = csv.reader(f4)
        for i in csv_reader_new:
            count += 1
            # print(i[1:])
            # if(i[0].isdigit()):
            #     f2.write(''.join(i[0])+','+''.join(i[1:]))
            # f2.write(''.join(i[0]) + ',' + ''.join(i[1:]))
            # else:
            #     print(i)
            # f2.write(i[0])
            newlist = []
            newlist.append([i[0], str(''.join(i[1:])).replace(',', ' ')])
            # print(''.join(i[1:]))
            writer.writerows(newlist)

# f.close()
# f2.close()
df = pd.read_csv(file+'_new.csv', header = None, names = ['id', 'total', 'fenci', 'topic', 'location'])
df.to_csv(file+'_new.csv', index = False)
print(total)
print(count)

number = 0
with open(file+'_new.csv', 'r', encoding='utf-8') as f5:
    csv_reader_try = csv.reader(f5)
    for i in csv_reader_try:
        number += 1
print(number)