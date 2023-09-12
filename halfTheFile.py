import csv

file = "data/combine/totallyCollectedData"

count = 0
with open(file+'_new.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    with open(file + '.csv', 'r', encoding='utf-8') as csvfile:
        readfile = csv.reader(csvfile)
        for i in readfile:
            if (count % 8 == 0):
                list = []
                list.append(i)
                writer.writerows([i])
            count += 1