# import csv
# import json
#
# def json_to_csv():
#     json_file = open("dataset.json", "r")
#     csv_file = open("datasetAfterFiltering.csv", "w", encoding='utf-8')
#
#     item_list = []
#     counter = 1
#     for line in json_file:
#         print("加载line： "+str(counter))
#         counter+=1
#         item_list.append(json.loads(line))
#     # item_list = json.load(json_file)
#     print("加载完成")
#     key_data = item_list[0].keys()
#     print("Assign Key Data Successfully")
#     value_data = [item.values() for item in item_list]
#     print("Assign Value Data Successfully")
#
#     #write csv file object
#     csv_writer = csv.writer(csv_file)
#     print("Start write stage. ")
#     #先写入表头字段数据
#     csv_writer.writerow(key_data)
#     print("Key data write in ")
#     #再写入表的值数据
#     csv_writer.writerows(value_data)
#     print("Value data write in")
#
#     csv_file.close()
#     json_file.close()
#
# if __name__=="__main__":
#     json_to_csv()
import json
import threading

def convertDict():
    # json file to be read
    filename = "0228"
    filebefore = "data/before/"+filename
    fileafter = "data/after/"+filename
    f = open(filebefore+".json", 'r', encoding='utf-8')
    print('filter begin')
    # json file to be written after filtering
    with open(fileafter+"t1.json",'w') as jsonFile:
        for line in f.readlines():
            dic = json.loads(line)
            if dic['tweet_locations']==[]:
                print('delete an element')
            elif(dic['tweet_locations'][0]['country_code']=='us')|(dic['tweet_locations'][0]['country_code']=='uk'):
                print('normal in US or UK')
                json.dump(dic, jsonFile)
                jsonFile.write('\n')
    f.close()
def convertDict2():
    filename = "0227"
    filebefore = "data/before/" + filename
    fileafter = "data/after/" + filename
    f = open(filebefore + ".json", 'r', encoding='utf-8')
    print('filter begin')
    # json file to be written after filtering
    with open(fileafter + "t1.json", 'w') as jsonFile:
        for line in f.readlines():
            dic = json.loads(line)
            if dic['tweet_locations'] == []:
                print('delete an element')
            elif (dic['tweet_locations'][0]['country_code'] == 'us') | (
                    dic['tweet_locations'][0]['country_code'] == 'uk'):
                print('normal in US or UK')
                json.dump(dic, jsonFile)
                jsonFile.write('\n')
    f.close()
def convertDict3(filename):
    # filename = "0226"
    filebefore = "data/before/" + filename
    fileafter = "data/after/" + filename
    f = open(filebefore + ".json", 'r', encoding='utf-8')
    print('filter begin')
    # json file to be written after filtering
    m = 1
    with open(fileafter + "t1.json", 'w') as jsonFile:
        for line in f.readlines():
            dic = json.loads(line)
            if dic['tweet_locations'] == []:
                # print('delete an element')
                m +=1
            elif (
                    dic['tweet_locations'][0]['country_code'] == 'us'
            ) | (
                    dic['tweet_locations'][0]['country_code'] == 'uk'
            ) | (
                    dic['tweet_locations'][0]['country_code'] == 'es'
            ) | (
                    dic['tweet_locations'][0]['country_code'] == 'it'
            ):
                # print('normal in US or UK')
                json.dump(dic, jsonFile)
                jsonFile.write('\n')
    f.close()
    print('delete '+str(m)+' elements')
if __name__=="__main__":
    # convertDict()
    # threads = [threading.Thread(target=convertDict()),
    #            threading.Thread(target=convertDict2()),
    #            threading.Thread(target=convertDict3())]
    # for t in threads:
    #     t.start()
    # convertDict3("0310")
    # for num in range(1,22):
    #     if (num < 10):
    #         convertDict3("040" + str(num))
    #         print('finish in: 040'+str(num)+'.json')
    #     else:
    #         convertDict3("04"+str(num))
    #         print('finish in: 04'+str(num)+'.json')
    # print('finish first part')
    # for num in range(1,8):
    #     if (num < 10):
    #         convertDict3("030" + str(num))
    #         print('finish in: 030'+str(num)+'.json')
    #     else:
    #         convertDict3("03"+str(num))
    #         print('finish in: 03'+str(num)+'.json')
    # convertDict3("0229")
    convertDict3("0501")
    print('finish all')