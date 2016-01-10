#!/usr/bin/python
#coding:utf-8

#判断list中有没有包含的字符串，exit退出

list = range(100)

while True:
    _input = raw_input('请输入一个数字： ')
    _in_list = 'Flase'
    if _input == 'exit':
        break
    for i in list:
        if int(_input) == i:
            _in_list = True
            break
    print _in_list

#实现len
_len = None
_list = [-1,-10,1,2,3,64,7,8,54,65,7]

for i in _list:
    if _len == None:
	_len = 0  
    _len += 1

print '列表的长度为%d' %_len

#实现max,min

#_max = 0 
#_min = 10000

_max = None 
_min = None

for i in _list:
    if _max == None:
	_max = i
    if _min == None:
	_min = i
    if i > _max:
	_max = i
    if i < _min:
	_min = i
print '列表中最大值为%d,最小值为%d' %(_max,_min)
