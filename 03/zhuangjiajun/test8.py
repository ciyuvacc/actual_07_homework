#!/usr/bin/python
#coding:utf-8

#练习8：'reboot' 字符串倒序（不能用切片）

_str = 'reboot'
new = ''
for i in _str:
    new = i + new
print new

new = []
for i in _str:
    new.insert(0,i)
print ''.join(new)
