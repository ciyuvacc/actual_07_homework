#!/usr/bin/python
#coding:utf-8
year = 0
ben = 10000
sum = 10000
while sum <= ben*2:
    year = year + 1
    sum = ben + ben * 0.0325 * year
print '实际需要%d年' %year
    
