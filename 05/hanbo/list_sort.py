#!/usr/bin/env python
#coding:utf8
list = [(1,4),(5,1),(2,3)]
list.sort(key=lambda i:i[0])
print "按每个元组的第0位从大到小排序结果为:" 
print list
list.sort(key=lambda i:i[1])
print "按每个元组的第1位从大到小排序结果为:" 
print list
