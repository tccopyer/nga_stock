import requests
from bs4 import BeautifulSoup
import re
import pymysql
import time

from pymysql.converters import escape_string as esing


conn=pymysql.connect(host='localhost',user='root',password='Swift666',database='database1')

cursor=conn.cursor()

page_url='https://bbs.nga.cn/thread.php?fid=706&page='




def get_url(page_url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    cookie ='taihe_bi_sdk_uid=5c964338fc2399cfc697b5b2e9a36d1b; ngacn0comUserInfo=%CE%D2%BE%AD%B3%A3%B7%A2%CC%FB	%E6%88%91%E7%BB%8F%E5%B8%B8%E5%8F%91%E5%B8%96	39	39		10	0	4	0	0	; taihe=8347969becddc4f9a1609f12f632b136; UM_distinctid=1776c4c9be21b4-0a8bf5abd37f84-33e3567-e1000-1776c4c9be3f0; ngaPassportUid=39346926; ngaPassportUrlencodedUname=%CE%D2%BE%AD%B3%A3%B7%A2%CC%FB; ngaPassportCid=783d790aea756373d1ca54a94ca3ef0f33d6f180; HMF_CI=737e3ea10127eaa871db7aa92fc76e63fb1fdb9539a9f0dda04aa2933e7e4c9af5; ngacn0comUserInfoCheck=f3b63085ebf5c5f18ea64983a33e31d9; ngacn0comInfoCheckTime=1628038650; CNZZDATA30043604=cnzz_eid=299767520-1610501593-https%3A%2F%2Fwww.baidu.com%2F&ntime=1628034524; lastvisit=1628039113; lastpath=/thread.php?fid=-7; bbsmisccookies={"uisetting":{0:"g",1:1628039412},"pv_count_for_insad":{0:-43,1:1628096468},"insad_views":{0:1,1:1628096468}}; _cnzz_CV30043604=forum|fid-7|0'
    headers = {"User-Agent": user_agent, "Cookie": cookie}
    session = requests.Session()
    res = session.get(page_url, headers=headers)
    soup = BeautifulSoup(res.content, 'lxml')
    return soup

#test1=get_url(page_url)

#housename_divs = test1.find_all('tbody')

def get_header(housename_divs):
    #n=1
    for i in housename_divs:
#
        mes=i.find_all('td',class_='c2')
        mes1=mes[0].find('a')##这里将标题内容储存了下来
        mes = mes1.get_text()
        ##content=re.findall('onclick=\"([^\"]*)\"',str(mes))[0]
        ## 获取title=“  ”中双引号之间的内容
        heat=i.find_all('td',class_='c1')
        heat1=heat[0].find('a')##这里将热度储存了下来
        heat=heat1.get_text()

        author=i.find_all('td',class_='c3')
        author1=author[0].find('a')##这里将作者储存了下来
        author=author1.get_text()


        timestamp = i.find_all('td', class_='c3')
        timestamp1 = timestamp[0].find('span', class_='silver postdate')  ##这里将作者储存了下来
        timestamp = int(timestamp1.get_text())



        sql1 = "INSERT INTO nga_test (mes,heat,author,timestamp) VALUES ('%s','%s','%s','%s')"%(esing(mes),heat,author,timestamp)
        sql2="UPDATE nga_test SET timestamp='%s',heat='%s' where mes ='%s'"% (timestamp,heat,esing(mes))
        try:
            cursor.execute(sql1)
            print('新加入')
        except:
            cursor.execute(sql2)
            print('已更新')
        conn.commit()



q=1
while q<100:

    page=get_url(page_url+str(q))

    housename_divs=page.find_all('tbody')
    get_header(housename_divs)
    print(q)
    q=q+1