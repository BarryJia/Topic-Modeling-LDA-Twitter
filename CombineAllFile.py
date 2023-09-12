import csv
import glob

def functionA(filename):
    count = 0
    with open('data/combine/totallyCollectedData.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        with open('data/after/'+filename+'.csv', 'r', encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile)
            for i in readfile:
                if(count > 0):
                    list = []
                    list.append(i)
                    writer.writerows([i])
                count += 1
if __name__ == '__main__':
    # functionA()
    csv_list = glob.glob('data/after/*.csv')
    print(u'共发现%s个CSV文件' % len(csv_list))
    count = 0
    with open('data/combine/totallyCollectedData.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        with open('data/after/0201_full.csv', 'r', encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile)
            for i in readfile:
                if (count == 0):
                    list = []
                    list.append(i)
                    writer.writerows([i])
                count += 1
    for i in csv_list:
        a = i.strip('data/after\\').strip('.csv')
        print(a)
        functionA(a)