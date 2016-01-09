#!/usr/bin/python
#coding:utf-8
dict = {}
list = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js']
for i in list:
    if i in dict:
	dict[i] += 1
    else:
	dict[i] = 1
print dict
