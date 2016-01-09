#!/usr/bin/python
#coding:utf-8
'''
用之前的list知识，实现reverse的功能
'''
#方法一
arr = [1,2,8,5,4]
print arr
for i in range((len(arr) - 1)/2):
    tmp = arr[i]
    arr[i] = arr[ -1 * i - 1 ]
    arr[ -1 * i - 1 ] = tmp
print arr

#方法二
arr = [1,2,8,5,4]
print arr
_list = []
for i in range(len(arr)):
    _list.append(arr.pop())
print _list

#方法三
arr = [1,2,8,5,4]
_list = arr[::-1]
print arr
print _list
