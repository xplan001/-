# -*- coding: utf-8 -*-
import openpyxl

 #创建excel文档
wb =openpyxl.Workbook()
sheet = wb['Sheet']
sheet['A1'] = '颜色'
sheet['B1'] = '版本'
x = 2
for i in range(10):
    sheet['A'+str(x)] = i+1
    sheet['B'+str(x)] = i+1
    x += 1

wb.save('测试写数据.xlsx')
 
 
def generate_excel(expenses):
    wb =openpyxl.Workbook()
    sheet = wb['Sheet']
    sheet['A1'] = 'Name'
    sheet['B1'] = 'levels'
    sheet['C1'] = 'times'
    sheet['D1'] = 'emails'
    sheet['E1'] = 'phones'
    x = 2
    for i in range(10):
        sheet['A'+str(x)] = i+1
        sheet['B'+str(x)] = i+1
        x += 1

    wb.save('Midas.xlsx')
 
