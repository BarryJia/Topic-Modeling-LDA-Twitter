import csv
import json

def json_to_csv(date):
    json_file = open("data/after/"+date+"t1.json", "r")
    csv_file = open("data/new/"+date+"t1.csv", "w", encoding='utf-8', newline='')

    item_list = []
    counter = 1
    for line in json_file:
        print("加载line： "+str(counter))
        counter+=1
        item_list.append(json.loads(line))
    # item_list = json.load(json_file)
    print("加载完成")
    key_data = item_list[0].keys()
    print("Assign Key Data Successfully")
    value_data = [item.values() for item in item_list]
    print("Assign Value Data Successfully")

    #write csv file object
    csv_writer = csv.writer(csv_file)
    print("Start write stage. ")
    #先写入表头字段数据
    csv_writer.writerow(key_data)
    print("Key data write in ")
    #再写入表的值数据
    csv_writer.writerows(value_data)
    print("Value data write in")
    csv_file.close()
    json_file.close()

if __name__=="__main__":
    # json_to_csv()
    for num in range(1,31):
        if (num < 10):
            json_to_csv("040" + str(num))
        else:
            json_to_csv("04"+str(num))
    print("Finished")