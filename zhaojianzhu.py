#coding=utf-8
#http://www.zhaojianzhu.com/ 的爬取

from bs4 import BeautifulSoup
import requests
import time
import openpyxl
from rec_excel import generate_excel

headers = {
    'Uesr-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Cookie':'ahCN_2132_saltkey=Ud88Ucg9; ahCN_2132_lastvisit=1573689861; Hm_lvt_2cba0a0cd4daa39dad1e500d6b31f4bf=1573693465; ahCN_2132_sid=Mt9NZ9; pgv_pvi=9982558364; pgv_info=ssi=s3451759545; ahCN_2132_st_p=0%7C1573693630%7C18445aaf7b0ea60ddadde2c5a08d846d; ahCN_2132_viewid=tid_255974; ahCN_2132_st_t=0%7C1573693892%7Cb8539728d932a3af4e74d28c80adac7d; ahCN_2132_forum_lastvisit=D_2_1573693508D_48_1573693552D_64_1573693589D_66_1573693605D_52_1573693609D_49_1573693892; ahCN_2132_visitedfid=49D52D66D64D48D2; ahCN_2132_lastact=1573693893%09home.php%09misc; ahCN_2132_sendmail=1; Hm_lpvt_2cba0a0cd4daa39dad1e500d6b31f4bf=1573693893',
}


url = "http://www.midasuser.cn/e/space/?userid=655998"

urls = ['http://www.zhaojianzhu.com/guojiaguifan/444?page={}'.format(str(i)) for i in range(1,22,1)]      

def get_url(url):
    try:
        web_data = requests.get(url,headers=headers)    #,data=None, data=payload
        time.sleep(2)
        web_data.encoding = 'utf-8'
        soup = BeautifulSoup(web_data.text,'lxml')

        url_lists = soup.select('tr > th > a')    #normalthread_255819 > tr > th > a

        # for url_list in zip(url_lists):
        #     data = {
        #     'url_list':'http://www.zhaojianzhu.com/' + url_list.get('href'),     
        #     }
        #     print(data)
            
        print(url_lists)
    except:
        print('页面加载异常')

if __name__ == '__main__':
    get_url(url)    



