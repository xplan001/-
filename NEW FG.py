#coding=utf-8
#建标库网站(http://www.jianbiaoku.com)结构最新规范的爬取

from bs4 import BeautifulSoup
import requests
import time
import xlsxwriter

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
    BookList = []
    for B_title,B_url,B_version,B_date in zip(Book_titles,Book_titles,Book_version,Book_date):
        data = {
            'B_title':B_title.get_text(),
            'B_url':'http://www.jianbiaoku.com/' + B_title.get('href'),
            'B_version':B_version.get_text(),
            'B_date':B_date.get_text(),
        }

        BookList.append(data)
        # print(data)
    return BookList
#BookList = {}

def generate_excel(expenses):
    workbook = xlsxwriter.Workbook('./GuiFan_data.xlsx')
    worksheet = workbook.add_worksheet()
 
    # 设定格式，等号左边格式名称自定义，字典中格式为指定选项
    # bold：加粗，num_format:数字格式
    bold_format = workbook.add_format({'bold': True})
    #money_format = workbook.add_format({'num_format': '$#,##0'})
    #date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})
 
    # 将二行二列设置宽度为15(从0开始)
    worksheet.set_column(1, 1, 15)
 
    # 用符号标记位置，例如：A列1行
    worksheet.write('A1', 'Name', bold_format)
    worksheet.write('B1', 'Urls', bold_format)
    worksheet.write('C1', 'versions', bold_format)
    worksheet.write('D1', 'dates', bold_format)

    row = 1
    col = 0
    for item in (expenses):
            # 使用write_string方法，指定数据格式写入数据
            worksheet.write_string(row, col, str(item['B_title']))
            worksheet.write_string(row, col + 1, item['B_url'])
            worksheet.write_string(row, col + 2, item['B_version'])
            worksheet.write_string(row, col + 3, item['B_date'])
           
            row += 1
    workbook.close()


if __name__ == '__main__':
    Ls1 = []
    for single_url in urls:
    
        Ls1.extend(get_Book(single_url))
        print(len(Ls1))             #get_Book(single_url)
    
    print(Ls1)                # len(Ls1)Ls1get_Book(url)
    generate_excel(Ls1)
