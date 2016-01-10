#!/usr/bin/python
#coding:utf-8

a = []
while True :
    _option = raw_input('请选择add或者do: ')
    if _option == 'add':
	_list = raw_input('please input a str: ')
	a.append(_list)
	print a
    if _option == 'do':
        if a == []:
	    print "所有事件已完成"
	    break
        print a.pop(0)
	print a
    else:
	print '请输入add或者do'
