# coding=utf-8
import pandas as pd
import math
import numpy as np




def once(file):
    df = pd.read_csv(file+'.csv', low_memory=False)

    from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


    #向量化
    n_features = 1000

    tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
                                    max_features=n_features,
                                    stop_words='english',
                                    max_df = 0.5,
                                    min_df = 10)
    tf = tf_vectorizer.fit_transform(df.item_definition)
    # print(df.id)


    from sklearn.decomposition import LatentDirichletAllocation

    n_topics = 10
    # LDA处理
    # lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=50,learning_method='online',learning_offset=50.,random_state=0)
    lda = LatentDirichletAllocation(n_components=n_topics, max_iter=100,

                                    learning_method='online',

                                    learning_offset=50.,

                                    random_state=0)
    # LDA模型训练
    lda.fit(tf)
    # nps=np.log(lda.components_)
    # print(nps)
    # npsDf=pd.DataFrame(nps)
    # npsDf.to_csv('term_topics.csv')
    pd.set_option('display.max_columns',None)
    pd.set_option('display.max_rows',None)
    print("test",lda.components_)
    topic_word_dist=lda.components_
    topic_word=pd.DataFrame(topic_word_dist)
    sum=topic_word.sum(axis=1)
    print(sum)
    p=topic_word.div(sum,axis=0)
    print(p)

    print(lda.components_)
    tlist = []
    file_topic = open(file+'_topics.txt', mode='w')
    def print_top_words(model, feature_names, n_top_words):
        for topic_idx, topic in enumerate(model.components_):   #model.components_:主题-词语;enumerate：同时获得索引和值
            print("Topic %d:" % topic_idx)
            print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))  #argsort()将topic中的元素从小到大排列，提取其对应的index
            tlist.append(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
            file_topic.write("Topic %d:" % topic_idx)
            file_topic.write('\n')
            file_topic.write(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
            file_topic.write('\n')

    n_top_words = 5
    tf_feature_names = tf_vectorizer.get_feature_names()  #文档集生产的词典
    print_top_words(lda, tf_feature_names, n_top_words)
    top_list = tlist


    #根据LDA运行结果，对文档分类
    doc_topic_dist = lda.transform(tf) #文档-主题矩阵
    arr=pd.DataFrame(doc_topic_dist)#将doc_topic_dist转化为DataFrame
    row=len(arr)  #获取总行数
    print("document,topic")
    dataindex=[]
    for i in range(0,row):
        doc=arr.loc[i,:]  #获取第i-1列数据
        doclst=list(doc)  #将series类型数据转换为列表
        i_argmax=doclst.index(max(doclst))   #列表中最大值对应的索引，即概率最大对应的topic
        dataindex.append([i_argmax, df.id[i], top_list[i_argmax]])
        # print(doc)
        # print(i,i_argmax)  #输出文档和对应的topic

    indexDf=pd.DataFrame(dataindex)
    indexDf.to_csv(file+'_doc_topics.csv', index = False)
    df = pd.read_csv(file+'_doc_topics.csv', header = None,  names = ['topic', 'id', 'words', 'location'])
    df.to_csv(file+'_doc_topics.csv', index = False)

once("/Users/jiashichao/Desktop/LWN/project/USA_byword")


