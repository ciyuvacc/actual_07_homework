#!/usr/bin/python
#coding:utf-8

#方法一 冒泡排序
#遍历整个list，依次将最大值放到最后
_list = [1,2,3,4,43,3,1,2,3]
for x in range(len(_list) - 1):
    for i in range(len(_list) - 1 - x):
        if _list[i] > _list[i + 1]:
       	    tmp = _list[i]
    	    _list[i] = _list[i + 1]
    	    _list[i + 1] = tmp
print _list


#方法二 插入排序
#将一个元素插入到有序的列表中，将第二个元素一次插入到已经排序的列表里
_list = [1,2,3,4,43,3,1,2,3]
for i in range(1, len(_list)):
    for i in range(i,0,-1):
        if _list[i] < _list[i - 1]:
	    tmp = _list[i]
	    _list[i] = _list[i - 1]
	    _list[i - 1] = tmp
	else:
	    break
print _list
