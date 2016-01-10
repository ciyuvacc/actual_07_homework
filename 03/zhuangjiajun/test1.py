#!/usr/bin/python
#coding:utf-8
'''
练习1:实现copy功能
'''
dict = {'zjj':'zhuangjiajun','ly':'liuying'}
dict1 = {}
for i in dict:
    dict1[i] = dict.get(i)
print dict
print dict1
