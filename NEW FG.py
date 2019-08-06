#coding=utf-8
#建标库网站(http://www.jianbiaoku.com)结构最新规范的爬取

from bs4 import BeautifulSoup
import requests
import time
import openpyxl

headers = {
    'Uesr-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Cookie':'ASP.NET_SessionId=noqaazpuurkfpoxrdxw0antp; zz_client_token=c0a6fa104e6949dcb691438037170d1c; Hm_lvt_ac3f24c58d6856a28f4da49c5ade057f=1564212652; Hm_lpvt_ac3f24c58d6856a28f4da49c5ade057f=1564221370',
}

url = "http://www.jianbiaoku.com/webarbs/list/120/1.shtml"
urls = ['http://www.jianbiaoku.com/webarbs/list/120/{}.shtml'.format(str(i)) for i in range(1,23,1)]

def get_Book(url,data=None):
    web_data = requests.get(url,headers=headers)
    time.sleep(1)
    web_data.encoding = 'utf-8'
    soup = BeautifulSoup(web_data.text,'lxml')

    Book_titles = soup.select('div.book_item > span > a')
    Book_version = soup.select('div.book_item > span.book_version')
    Book_date = soup.select('div.book_item > span.book_date')
    
    #print(Book_titles,'\n',Book_version,'\n',Book_date) 

    for B_title,B_url,B_version,B_date in zip(Book_titles,Book_titles,Book_version,Book_date):
        data = {
            'B_title':B_title.get_text(),
            'B_url':'http://www.jianbiaoku.com/' + B_title.get('href'),
            'B_version':B_version.get_text(),
            'B_date':B_date.get_text(),
        }

        print(data)

#BookList = {}

for single_url in urls:
    get_Book(single_url)
    #BookList.update(get_Book(single_url))

    #print(BookList)
