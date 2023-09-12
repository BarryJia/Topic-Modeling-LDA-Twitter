# coding=utf-8


import jieba
import pandas as pd

file = "data/combine/totallyCollectedData_small"


df = pd.read_csv(file+"_new.csv")  # read data

def stopwordslist(filepath):
    # print('stopwordslist')
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 进行分词
def seg_sentence(sentence):
    # print("seg_sentence")
    sentence_seged = jieba.cut(sentence.strip())
    # print("/ ".join(sentence_seged))
    stopwords = stopwordslist('stopwords_e_2.txt')  # stopwords directory
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

inputs=df["total"]
# inputs = df
id = df["id"]

#新建分词结果列
outputs =df["fenci"]

line_seg=[]
# for line in inputs:
for i in range(len(inputs)):
    # print(type(line))
    line = inputs[i]
    line_seg.append([seg_sentence(line), id[i]])
    # line_seg.append(seg_sentence(line))
    # outputs.write(line_seg + '\n')
# print(line_seg)
# name=['fenci']
# test=pd.DataFrame(columns=name,data=line_seg)
name=['fenci', 'id']
print('almost')
test=pd.DataFrame(columns=name,data=line_seg)

# print(test)
print('transfer to csv file')
test.to_csv(file+'_stopwords.csv',encoding='utf-8')
