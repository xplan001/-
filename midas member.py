#coding=utf-8
#http://www.midasuser.cn/webclass/ 的爬取

from bs4 import BeautifulSoup
import requests
import time
import openpyxl
from rec_excel import generate_excel

headers = {
    'Uesr-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Cookie':'Hm_lvt_6a9fd242d218ca3a0e40f6a3671f9318=1565057145,1566177297; cfccamlusername=xplan; cfccamluserid=651597; cfccamlgroupid=1; cfccamlrnd=w0M6x3PlzC9aDXAQKimT; cfccamlauth=2bcab83dd65b07a6f9e7680d0ef842c6; cfccacheckplkey=1566178956%2Cf929dbb5893f0277c1963b3eb7344328%2C097f57ec6e40b3e396ba8de305101db0; Hm_lpvt_6a9fd242d218ca3a0e40f6a3671f9318=1566181569; cfccadospacevstats856=1',
}


url = "http://www.midasuser.cn/e/space/?userid=655998"
#urls = ['http://www.midasuser.cn/e/space/?userid={}'.format(str(i)) for i in range(855,1019,1)]  
#urls = ['http://www.midasuser.cn/e/space/?userid={}'.format(str(i)) for i in range(9501,10496,1)]
urls = ['http://www.midasuser.cn/e/space/?userid={}'.format(str(i)) for i in range(655020,656019,1)]       #656309

def get_url(url):
    web_data = requests.get(url,headers=headers)    #,data=None, data=payload
    time.sleep(2)
    web_data.encoding = 'utf-8'
    soup = BeautifulSoup(web_data.text,'lxml')

    Book_names = soup.select('tr > td')[6]
    Book_levels = soup.select('tr > td')[8]
    Book_times = soup.select('tr > td')[10]
    Book_emails = soup.select('tr > td')[12]
    Book_phones = soup.select('tr > td')[16]


    #print(Book_names,Book_levels,Book_times,Book_emails,Book_phones)

    for B_name,B_level,B_time,B_email,B_phone in zip(Book_names,Book_levels,Book_times,Book_emails,Book_phones):
        data = {
        # 'B_id':url[17:28],
        'B_name':Book_names.get_text().lstrip().rstrip(),
        'B_level':Book_levels.get_text().lstrip().rstrip(),
        'B_time':Book_times.get_text().lstrip().rstrip(),
        'B_email':Book_emails.get_text().lstrip().rstrip(),
        'B_phone':Book_phones.get_text().lstrip().rstrip(),
        }
        return data

#urls = get_url(url)

# get_url(url)
if __name__ == '__main__':
    Ls1 = []
    for single_url in urls:
        
        Ls1.append(get_url(single_url))
        print(len(Ls1))

    print(Ls1) # len(Ls1)Ls1
    generate_excel(Ls1)
        # print(get_url(single_url))



