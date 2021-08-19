import tensorflow as tf
from tensorflow import keras

import numpy as np

from tensorflow.keras import layers
import tensorflow_hub as hub

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
x_train_tokens = []
##进行分词处理
for line in list_contents:

    words = pseg.cut(line)
    line0 = []
    for myword in words:  # 获取初次分词结果中的每一个词
        if not (myword.word in f_stop_seg_list):
            line0.append(myword.word)
            #try:
    test.append(' '.join(line0))
print('完成分词')
print(test)
###拿到的testlist 相当于 例子中的 get words

###这里是已经获得编码后的词汇了
'''embedding_layer = layers.Embedding(1000, 5)

result = embedding_layer(tf.constant([1,3,6]))
result.numpy()
print(result)

result = embedding_layer(tf.constant([[0,1,2],[3,4,5]]))
result.shape

print(result)'''




embed = hub.load("https://hub.tensorflow.google.cn/google/tf2-preview/gnews-swivel-20dim/1")
embeddings = embed(["狗 不是 猫", "dog is in the fog"])

print(embeddings)