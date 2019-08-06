#coding=utf-8
#http://www.midasuser.cn/webclass/ 视频的爬取

from bs4 import BeautifulSoup
import requests
import time
import openpyxl

headers = {
    'Uesr-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Cookie':'Hm_lvt_6a9fd242d218ca3a0e40f6a3671f9318=1565057145; cfccamlusername=xplan; cfccamluserid=651597; cfccamlgroupid=1; cfccamlrnd=FONh73Q1ePFEeOjNIl2f; cfccamlauth=74a5fefba11927822c70b0d2a95e6b33; cfccacheckplkey=1565072859%2Cf5dd329ddb20b75965eab7331905e7a3%2C41f3b01819d1b35df280ad7fa63efac1; Hm_lpvt_6a9fd242d218ca3a0e40f6a3671f9318=1565072970',
}


#url = "http://www.midasuser.cn/webclass/building/"
#url = "http://www.midasuser.cn/e/member/list/index.php?page=0&totalnum=15715"
urls = ['http://www.midasuser.cn/e/member/list/index.php?page={}&totalnum=15715'.format(str(i)) for i in range(0,15715,1)]
#url1 = "http://www.midasuser.cn/webclass/building/2018-08-20/226.html"

def get_url(url):
    web_data = requests.get(url,headers=headers)    #,data=None, data=payload
    time.sleep(2)
    web_data.encoding = 'utf-8'
    soup = BeautifulSoup(web_data.text,'lxml')

    Book_titles = soup.select('tr > td > a')[:20]
    #Book_titles = soup.find_all('tr')[1:21]

    #print(Book_titles)
 
    for B_id,B_title,B_url in zip(Book_titles,Book_titles,Book_titles):
        data = {
        'B_id':B_title.get('href')[17:28],
        'B_title':B_title.get_text()[11:].rstrip(),
        'B_url':'http://www.midasuser.cn' + B_title.get('href'),
        }
        print(data)
    

#urls = get_url(url)

#get_url(url)

for single_url in urls:
    get_url(single_url)
