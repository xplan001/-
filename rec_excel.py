# -*- coding: utf-8 -*-
import xlsxwriter
 
#生成excel文件
def generate_excel(expenses):
    workbook = xlsxwriter.Workbook('./rec_data.xlsx')
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
    worksheet.write('B1', 'levels', bold_format)
    worksheet.write('C1', 'times', bold_format)
    worksheet.write('D1', 'emails', bold_format)
    worksheet.write('E1', 'phones', bold_format)
    # worksheet.write('F1', 'Url', bold_format)
    row = 1
    col = 0
    for item in (expenses):
            # 使用write_string方法，指定数据格式写入数据
            worksheet.write_string(row, col, str(item['B_name']))
            worksheet.write_string(row, col + 1, item['B_level'])
            worksheet.write_string(row, col + 2, item['B_time'])
            worksheet.write_string(row, col + 3, item['B_email'])
            worksheet.write_string(row, col + 4, item['B_phone'])
            # worksheet.write_string(row, col + 5, item['id_2_doc'])
            row += 1
    workbook.close()
 
 
# if __name__ == '__main__':
#     rec_data = [{'B_name': 'SJY123', 'B_level': '普通会员', 'B_time': '2017-09-17 15:47:08', 'B_email': '1193904601@qq.com', 'B_phone': ''},  {'B_name': '司马毅', 'B_level': '普通会员', 'B_time': '2017-10-08 09:42:26', 'B_email': '939675940@qq.com', 'B_phone': ''}]
#     generate_excel(rec_data)