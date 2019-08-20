#-*- coding=utf-8 -*-
import fmovice

#movices = 'ʳ��' #input(':')

a = fmovice.Search_Movice("我不是药神")

for movie in a:
	files = open('movices.txt','a')
	files.write(movie)
	files.close()

