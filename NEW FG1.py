#coding=utf-8
#国家工程建设标准化信息网(http://ccsn.gov.cn/)结构最新规范的爬取

from bs4 import BeautifulSoup
import requests
import time
import openpyxl

headers = {
    'Uesr-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Cookie':'ASP.NET_SessionId=5oj4ue55iqmutoz3x5hhva45',
}

payload = {'ID_ucForceStandardList$kewordtxt': '', 'ID_ucForceStandardList$UcPager1$listPage': 3}
#http://ccsn.gov.cn/Xxbz/ForceStandardList.aspx?actForceStandardList_StandardType=%u5de5%u7a0b%u884c%u6807&actForceStandardList_IsChoosTrade=true&actForceStandardList_TradeorPlace=%u5efa%u7b51%u5de5%u7a0b
#http://ccsn.gov.cn/Xxbz/ForceStandardList.aspx?actForceStandardList_StandardType=%b9%a4%b3%cc%b9%fa%b1%ea&actForceStandardList_IsFzBz=false&actForceStandardList_IsChoosTrade=false

url = "http://ccsn.gov.cn/Xxbz/ForceStandardList.aspx?actForceStandardList_StandardType=%b9%a4%b3%cc%b9%fa%b1%ea&actForceStandardList_IsFzBz=false&actForceStandardList_IsChoosTrade=false"
#urls = ['http://www.jianbiaoku.com/webarbs/list/120/{}.shtml'.format(str(i)) for i in range(1,23,1)]

def get_Book(url,data=None):
    web_data = requests.get(url,headers=headers, data=payload)
    #time.sleep(5)
    #web_data.encoding = 'utf-8'
    soup = BeautifulSoup(web_data.text,'lxml')

    Book_titles = soup.select('a[target="_blank"]')[:30]
    #Book_titles = Book_titles1[:30]

    for B_title,B_url,B_version in zip(Book_titles,Book_titles,Book_titles):
        data = {
        'B_title':B_title.get_text().split('〗',1)[1],
        'B_url':'http://ccsn.gov.cn/' + B_title.get('href'),
        'B_version':B_title.get_text().split('〗',1)[0].replace('〖',''),
        }
        print(data)

get_Book(url)


#print(Book_titles)

# def get_Book(url,data=None):
#     web_data = requests.get(url,headers=headers)
#     time.sleep(5)
#     web_data.encoding = 'utf-8'
#     soup = BeautifulSoup(web_data.text,'lxml')

#     Book_titles = soup.select('div.book_item > span > a')
#     Book_version = soup.select('div.book_item > span.book_version')
#     Book_date = soup.select('div.book_item > span.book_date')
    
#     #print(Book_titles,'\n',Book_version,'\n',Book_date) 

#     for B_title,B_url,B_version,B_date in zip(Book_titles,Book_titles,Book_version,Book_date):
#         data = {
#             'B_title':B_title.get_text(),
#             'B_url':'http://www.jianbiaoku.com/' + B_title.get('href'),
#             'B_version':B_version.get_text(),
#             'B_date':B_date.get_text(),
#         }

#         print(data)

# for single_url in urls:
#     get_Book(single_url)

