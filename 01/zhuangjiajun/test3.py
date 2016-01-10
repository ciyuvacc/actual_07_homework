#!/usr/bin/python
#coding:utf-8
count = 0
sum = 0
num = raw_input('请输入一个数字: ')
while num != '':
    sum = sum + int(num)
    count = count + 1.0
    num = raw_input('请输入一个数字: ')
avg =  sum / count 
print '所有数字的平均值为:%.1f' %avg

