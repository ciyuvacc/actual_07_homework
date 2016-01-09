#!/usr/bin/python
#coding:utf-8
#year = raw_input('请输入数字: ')
while True :
    year = int(raw_input('请输入数字: '))
    if year % 100 == 0 and year % 400 == 0:
        print '%d为闰年' %year
        break
    elif year % 100 != 0 and year % 4 == 0:
        print '%s为闰年' %year
	break
    else :
	print '%d不是闰年请输入数字' %year
 	#year = raw_input("%s不是闰年请输入数字: " %year) 

