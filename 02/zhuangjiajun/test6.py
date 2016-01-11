#!/usr/bin/python
#coding:utf-8
'''
练习6：一个序列[1,2,3,4,2,12,3,4,14,3,21,2,2,3,4111,22,3333,4]
求第二个4的索引值
'''
_str = 4
_list = [1,2,3,4,2,12,3,4,14,3,21,2,2,3,4111,22,3333,4,5]
count = 0
i = 0
 
while i < len(_list) - 1 :
    a = _list.index(_str,i)
    count += 1
    i = a + 1
    print '4的第%s个索引值为%s' %(count,a)

    
