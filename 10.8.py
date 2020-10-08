import random
import requests
from bs4 import BeautifulSoup
import flask

def connect():
    user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]
    headers = {'User-Agent': random.choice(user_agent)}
    def get_user_agent():
        return random.choice(user_agent)



import pymysql

DBHOST = 'localhost'
DBUSER = 'root'
DBPASS = '123187'
DBNAME = 'lw'
db = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
print('连接成功')
cur = db.cursor()
cur.execute("DROP TABLE IF EXISTS shuju")
sql = 'CREATE TABLE shuju(标题 TEXT,序号 VARCHAR(20),作者 TEXT,分类 TEXT,时间 VARCHAR(20),下载链接 TEXT)'
cur.execute(sql)
print('表格创建成功')

import time
time.sleep(3)

# requests.adapters.DEFAULT_RETRIES = 5

url = 'https://arxiv.org/list/cs.AI/pastweek?show=245'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text, 'lxml')

data1 = soup.select('#dlpage > dl > dd > div > div.list-title.mathjax')
data2 = soup.select('#dlpage > dl > dt > span > a:nth-child(1)')
data3 = soup.select('#dlpage > dl > dd > div > div.list-authors')
data4 = soup.select('#dlpage > dl > dd > div > div.list-subjects > span.primary-subject')
date = soup.select('#dlpage > ul > li > a')
data6 = soup.select('#dlpage > dl > dt > span > a:nth-child(2)')
for item5 in date:
    i5 = item5.get_text()
    i1 = data1.pop(0).get_text()
    i1 = i1.strip('\nTitle: ')
    i2 = data2.pop(0).get_text()
    i2 = i2.strip('arXiv: ')
    i3 = data3.pop(0).get_text()
    i3 = i3.strip('\nAuthors:\n')
    i3 = i3.replace("\n", "")
    i4 = data4.pop(0).get_text()
    i6 = data6.pop(0).get('href')
    result = (i1, i2, i3, i4, i5, 'https://arxiv.org'+i6)
    # print(result)
    sql = 'INSERT INTO shuju(标题, 序号, 作者, 分类, 时间, 下载链接) VALUES (%s,%s,%s,%s,%s,%s)'
    values = (data1.pop(0).get_text().strip('\nTitle: '), data2.pop(0).get_text().strip('arXiv: '), data3.pop(0).get_text().strip('\nAuthors:\n').replace("\n", ""),data4.pop(0).get_text(), item5.get_text(),'https://arxiv.org'+data6.pop(0).get('href')),(data1.pop(0).get_text().strip('\nTitle: '), data2.pop(0).get_text().strip('arXiv: '), data3.pop(0).get_text().strip('\nAuthors:\n').replace("\n", ""),data4.pop(0).get_text(), item5.get_text(),'https://arxiv.org'+data6.pop(0).get('href'))
    cur.executemany(sql, values)
    db.commit()
print('数据插入成功')

def chaxun():
    while 1:
      shuru = input('输入（输入“退出”退出）')
      if shuru == '退出':
          break
      else:
          word = '%' + shuru + '%'
          cur.execute("select * from shuju where 标题 like '%%%s%%'" % (word))
          data = cur.fetchall()
          print(data)

if __name__ == '__main__':
    chaxun()

db.close()
