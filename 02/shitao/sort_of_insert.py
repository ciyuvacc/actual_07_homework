#!/usr/bin/env python
#coding=utf-8

arr = [2,5,3,1,33,2,12,45,23,12,546,-1,9,900,-100,33,44,22]
for i in range(len(arr)):
    for j in range(i)[::-1]: # 将定位数字的索引值倒序，依次向前循环比较
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j] # 如果当前值比前一个值大，值互相交换
	    print arr
print "the sorted list is %s" %arr


'''
评注:
1. 程序执行错误，原因第10行使用的temp在第一执行时并没有在第7行定义(5>2跳过)

list_1 = [2,5,3,1,33,2,12,45,23,12,546,-1,9,900,-100,33,44,22]
for i in range(len(list_1)):
    for j in range(i, 0, -1):
        if list_1[j] < list_1[j-1]:
            list_1[j],list_1[j-1] = list_1[j-1],list_1[j]
        else:
            break

print list_1


加油
'''
