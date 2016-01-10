#!/usr/bin/python
#coding:utf-8
'''
index 从列表中找出某个值，返回第一个匹配项的索引位置
不存在的话，会报错，可以先用in检测
'''
_arr = [1,2,'a',3,5,1,56,45,234,6,7,234]
_str = 77
if _str not in _arr:
    print '%s not in list' %_str
else : 
    print _arr.index(_str)


