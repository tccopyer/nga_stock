# *- coding: utf-8 -*-
###作者：
import os
import pandas as pd
import jieba.posseg as pseg
import pickle
import pymysql

import tushare as ts
pro = ts.pro_api()
#选取30个股票，做成列表
pro = ts.pro_api('ec3d7415bf3dfebf0f27b1e5a9805f809b083fb1f8590c8c2bdc633f')
os.chdir(r'C:\Users\666\Desktop\temp')

stopwords_path = r'stopword.txt'


conn=pymysql.connect(host='localhost',user='root',password='Swift666',database='database1')

cursor=conn.cursor()

#engine=create_engine('mysql://root:Swift666@localhost:3306/record1')



sql='select ts_code from concept_index'
cursor.execute(sql)

result=cursor.fetchall()

conn.close

list_concept=[]
for i in result:
    list_concept.append(i[0])
df = pro.ths_member(ts_code='885835.TI')
print(df)

for q in list_concept:
    print(q)
    df = pro.ths_member(ts_code=q)
    res = df.to_csv(q+'.csv', header=True)

