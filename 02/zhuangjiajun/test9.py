#!/usr/bin/python
#coding:utf-8
_list = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
__list = []
for i in _list : 
    if i not in __list:
	__list.append(i)
print _list
print __list
