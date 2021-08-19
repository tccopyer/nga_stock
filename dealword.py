# *- coding: utf-8 -*-

###作者：

import os
#import pandas as pd
import jieba.posseg as pseg
import pickle
import pymysql

os.chdir(r'C:\Users\666\Desktop\temp')
stopwords_path = r'stopword.txt'


conn=pymysql.connect(host='localhost',user='root',password='Swift666',database='database1')

cursor=conn.cursor()

#engine=create_engine('mysql://root:Swift666@localhost:3306/record1')



sql='select mes from nga_test where score is not NULL'
try:
    cursor.execute(sql)

    result=cursor.fetchall()
except:
    exit()
conn.close
###将数据库数据读为列表
list_contents=[]
for i in result:
    list_contents.append(i[0])


#把预处理的数据转换为列表

#list_label=df['label'].values.tolist()
#首先读取停用词表
f_stop = open(stopwords_path, encoding='utf-8')  # 打开停用词词表
try:
    f_stop_text = f_stop.read()  # 获取停用词词表中的内容
finally:
    f_stop.close()
f_stop_seg_list = f_stop_text.split('\n')
test = []
##进行分词处理
for line in list_contents:
    words = pseg.cut(line)
    line0 = []
    for myword in words:  # 获取初次分词结果中的每一个词
        if not (myword.word in f_stop_seg_list):
            line0.append(myword.word)
    test.append(line0)
print('完成分词')
print(test)

'''
# VECTOR_DIR = 'vectors.bin'
####贝叶斯相关参数
MAX_SEQUENCE_LENGTH = 100
EMBEDDING_DIM = 200
TEST_SPLIT = 0.2
print('(1) load texts...')  # 加载所需的文件
train_texts = test
train_labels = list_label
test_texts = open('test_text.txt').read().split('\n')
total_texts=train_texts+test_texts
print('(2) doc to var...')
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
count_v0 = CountVectorizer();
counts_all = count_v0.fit_transform(total_texts);
count_v1 = CountVectorizer(vocabulary=count_v0.vocabulary_);
counts_train = count_v1.fit_transform(train_texts);
print("the shape of train is " + repr(counts_train.shape))
count_v2 = CountVectorizer(vocabulary=count_v0.vocabulary_);
counts_test = count_v2.fit_transform(test_texts);
print("the shape of test is " + repr(counts_test.shape))
# 这里需要保存好几个模型
tfidftransformer = TfidfTransformer();
train_data = tfidftransformer.fit(counts_train).transform(counts_train);
test_data = tfidftransformer.fit(counts_test).transform(counts_test);
feature_path = 'feature.pkl'
tfi_path = 'tfi.pkl'
model_path = 'data_model.pkl'
with open(feature_path, 'wb') as fw:
    pickle.dump(count_v0.vocabulary_, fw)
with open(tfi_path, 'wb') as tfiw:
    pickle.dump(tfidftransformer, tfiw)
x_train = train_data
y_train = list_label
x_test = test_data
# y_test = test_labels
print('(3) Naive Bayes...')
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
###训练模型
clf = MultinomialNB(alpha=0.01)
clf.fit(x_train, y_train);
####保存模型
with open(model_path, 'wb') as mp:
    pickle.dump(clf, mp)
print('建模完成')
'''






'''preds = clf.predict(x_test);
num = 0
preds = preds.tolist()
print(preds)'''