#!/usr/bin/python
#coding:utf-8
sum = 0
num = raw_input('请输入数字or字母pc: ')

while num != 'pc':
    sum = sum + int(num)
    num = raw_input('请输入数字or字母pc: ')
print '输入所有数字之和为:%d' %sum

    
