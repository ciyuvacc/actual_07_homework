#!/usr/bin/env python
#coding:utf8
list = [(1,4),(5,1),(2,3)]
list.sort(key=lambda i:i[0])
print "按每个元组的第0位从大到小排序结果为:" 
print list
list.sort(key=lambda i:i[1])
print "按每个元组的第1位从大到小排序结果为:" 
print list

'''
ok, 没有问题，但是不是咱们想要的，咱们的题目是使用list中每个元素(小list)中最大的值进行排序
注意避免使用关键字或内置变量定义为自己的变量名
num_list =[(1,4),(5,1),(2,3)]

#1
print sorted(num_list,key=lambda n:max(n))

#2
sorted(num_list, key=lambda a: a[0] if a[0]>a[1] else a[1])

#3
sorted(num_list, cmp=lambda x, y: 1 if max(x) > max(y) else (0 if max(x) > max(y) else -1))
'''
