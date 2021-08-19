# *- coding: utf-8 -*-

'''本程序将词汇进行分词后初步的建立字典程序，
并变成一个csv文件 也可以写入数据库'''


###作者：第一资本家

import os
import jieba.posseg as pseg
import pymysql
'''将原始数据从数据库读出来，并按照列 写入不同的列表'''
os.chdir(r'C:\Users\666\Desktop\temp')
stopwords_path = r'stopword.txt'
conn=pymysql.connect(host='localhost',user='root',password='Swift666',database='database1')
cursor=conn.cursor()
sql='select mes from nga_test'
sql1='select name,symbol from stock_basic'
try:
    cursor.execute(sql)
    result=cursor.fetchall()
    cursor.execute(sql1)
    result1=cursor.fetchall()
except:
    exit()
conn.close
###将数据库数据读为列表
mes_contents=[]
for i in result:
    mes_contents.append(i[0])

symbol=[]
name=[]

for i in result1:
    name.append(i[0])
    symbol.append(i[1])
print(name)

####3直接将这些信息填入到停用词列表里



#首先读取停用词表
f_stop = open(stopwords_path, encoding='utf-8')  # 打开停用词词表
try:
    f_stop_text = f_stop.read()  # 获取停用词词表中的内容
finally:
    f_stop.close()
f_stop_seg_list = f_stop_text.split('\n')

print(f_stop_seg_list)
test = []

##进行分词处理
for line in mes_contents:

    words = pseg.cut(line)
    line0 = []
    for myword in words:  # 获取初次分词结果中的每一个词
        if not (myword.word in f_stop_seg_list):
            line0.append(myword.word)
    test.append(line0)
print('完成分词')
print(test)

'''主函数，传参进入分好的词汇'''
def build_dic(data_list):
    dictionary = dict()
    index=0
    index_list=[]
    dic_value=[]
    for words in data_list:
        for word in words:
            if word in dic_value:
                pass
            else:
                index=index+1
                index_list.append(index)
                dic_value.append(word)
    dictionary=dict(zip(dic_value,index_list))

    return  dictionary

###下午测试
a=build_dic(test)
print(a)


with open('temp.txt','w') as f:

    f.write(str(a))
#######在此之前 要先将股票信息 包括代码筛