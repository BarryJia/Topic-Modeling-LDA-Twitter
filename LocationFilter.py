import csv

def convertDict3(filename):
    count = 0
    with open('data/locationSegmentation/US_totally_collected.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        with open('data/combine/'+filename+'.csv', 'r', encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile)
            for i in readfile:
                if (count == 0):
                    list = []
                    list.append(i)
                    writer.writerows([i])
                elif(count>0):
                    c = eval(i[7].strip('[').strip(']'))
                    # print(c)
                    if isinstance(c, tuple):
                        if(c[0]['country_code'] == 'us'):
                            list = []
                            list.append(i)
                            writer.writerows([i])
                    elif isinstance(c,dict):
                        if (c['country_code'] == 'us'):
                            list = []
                            list.append(i)
                            writer.writerows([i])
                count += 1
def convertDict2(filename):
    count = 0
    with open('data/locationSegmentation/UK_totally_collected.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        with open('data/combine/'+filename+'.csv', 'r', encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile)
            for i in readfile:
                if (count == 0):
                    list = []
                    list.append(i)
                    writer.writerows([i])
                elif(count>0):
                    c = eval(i[7].strip('[').strip(']'))
                    # print(c)
                    if isinstance(c, tuple):
                        for i in range(len(c)):
                            if(c[i]['country_code'] == 'uk'):
                                list = []
                                list.append(i)
                                writer.writerows([i])
                    elif isinstance(c,dict):
                        if (c['country_code'] == 'uk'):
                            list = []
                            list.append(i)
                            writer.writerows([i])
                count += 1
def convertDict1(filename):
    count = 0
    with open('data/locationSegmentation/ES_totally_collected.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        with open('data/combine/'+filename+'.csv', 'r', encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile)
            for i in readfile:
                if (count == 0):
                    list = []
                    list.append(i)
                    writer.writerows([i])
                elif(count>0):
                    c = eval(i[7].strip('[').strip(']'))
                    # print(c)
                    if isinstance(c, tuple):
                        if(c[0]['country_code'] == 'es'):
                            list = []
                            list.append(i)
                            writer.writerows([i])
                    elif isinstance(c,dict):
                        if (c['country_code'] == 'es'):
                            list = []
                            list.append(i)
                            writer.writerows([i])
                count += 1
def convertDict0(filename):
    count = 0
    with open('data/locationSegmentation/IT_totally_collected.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        with open('data/combine/'+filename+'.csv', 'r', encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile)
            for i in readfile:
                if (count == 0):
                    list = []
                    list.append(i)
                    writer.writerows([i])
                elif(count>0):
                    c = eval(i[7].strip('[').strip(']'))
                    # print(c)
                    if isinstance(c, tuple):
                        if(c[0]['country_code'] == 'it'):
                            list = []
                            list.append(i)
                            writer.writerows([i])
                    elif isinstance(c,dict):
                        if (c['country_code'] == 'it'):
                            list = []
                            list.append(i)
                            writer.writerows([i])
                count += 1
if __name__=="__main__":
    convertDict3("totallyCollectedData")
    convertDict2("totallyCollectedData")
    convertDict1("totallyCollectedData")
    convertDict0("totallyCollectedData")
    print('finish all')