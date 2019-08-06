#coding=utf-8
#http://www.midasuser.cn/webclass/ 视频的爬取

from bs4 import BeautifulSoup
import requests
import time
import openpyxl

headers = {
    'Uesr-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Cookie':'ASP.NET_SessionId=5oj4ue55iqmutoz3x5hhva45',
}


#url = "http://www.midasuser.cn/webclass/building/"
url = "http://www.midasuser.cn/index_9.html"
urls = ['http://www.midasuser.cn/index_{}.html'.format(str(i)) for i in range(2,13,1)]
#url1 = "http://www.midasuser.cn/webclass/building/2018-08-20/226.html"

def get_url(url):
    web_data = requests.get(url,headers=headers)    #,data=None, data=payload
    #time.sleep(5)
    web_data.encoding = 'utf-8'
    soup = BeautifulSoup(web_data.text,'lxml')

    Book_titles = soup.select('div.item > div.meta > div.title > h2 > a')
 
    for B_title,B_url in zip(Book_titles,Book_titles):
        data = {
        'B_title':B_title.get_text(),
        'B_url':'http://ccsn.gov.cn/' + B_title.get('href'),
        }
        print(data)
    

#urls = get_url(url)

get_url(url)

for single_url in urls:
    get_url(single_url)

# def get_url1(url1):
#     web_data = requests.get(url,headers=headers)    #,data=None, data=payload
#     #time.sleep(5)
#     web_data.encoding = 'utf-8'
#     soup = BeautifulSoup(web_data.text,'lxml')

#     Book_titles = soup.select('div.area > div.meihua_2 > p')

#     print(Book_titles)
 
    # for B_title,B_url in zip(Book_titles,Book_titles):
    #     data = {
    #     'B_title':B_title.get_text(),
    #     'B_url':'http://ccsn.gov.cn/' + B_title.get('href'),
    #     }
    #     print(data)


#get_url1(url1)