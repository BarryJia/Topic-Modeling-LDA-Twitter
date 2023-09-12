import csv
import glob

def functionA(filename):
    count = 0
    with open('data/TimeSegmentation/April_26_30/April_26_30_OriginalData.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        with open('data/new/April_26_31/'+filename+'.csv', 'r', encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile)
            for i in readfile:
                if(count > 0):
                    list = []
                    list.append(i)
                    writer.writerows([i])
                count += 1
if __name__ == '__main__':
    # functionA()
    csv_list = glob.glob('data/new/April_26_31/*.csv')
    print(u'共发现%s个CSV文件' % len(csv_list))
    count = 0
    with open('data/TimeSegmentation/April_26_30/April_26_30_OriginalData.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        with open('data/new/April_26_31/0426t1.csv', 'r', encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile)
            for i in readfile:
                if (count == 0):
                    list = []
                    list.append(i)
                    writer.writerows([i])
                count += 1
    for i in csv_list:
        a = i.strip('data/new/April_26_31\\').strip('.csv')
        print(a)
        functionA(a)