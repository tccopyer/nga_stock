
import requests
from bs4 import BeautifulSoup
import re

page_url='http://youhui.bacaoo.com'

def get_url(page_url):
    res = requests.get(page_url)
    soup = BeautifulSoup(res.content, 'lxml')
    return soup
test1=get_url(page_url)

housename_divs = test1.find_all('div',class_='title')
n=1
for i in housename_divs:
    mes=i.find_all('a')
    content=re.findall('title=\"([^\"]*)\"',str(mes))[0]
    if "京东" in content:
        print(str(n)+'命中关键信息')
    ## 获取title=“  ”中双引号之间的内容
    print(str(n)+"    "+content)
    n = n + 1

list2=[['你们', '都', '挂', '了', '什么', '价买', '盐湖'], ['报', '，', '腾讯', '盘前', '涨', '5', '个', '点', '了'], ['看', '了', '看', '好像', '没', '人', '讨论', '农业', '股']]
print(len(list2))
for line in list2:
    print(len(line))