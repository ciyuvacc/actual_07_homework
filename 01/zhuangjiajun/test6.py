#!/usr/bin/python
#coding:utf-8
num = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
maxnum = 0
for i in num :
    if i > maxnum:
        maxnum = i
print '这个list的最大值为:%d' %maxnum
