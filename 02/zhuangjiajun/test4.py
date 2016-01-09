#!/usr/bin/python
#coding:utf-8

#将列表中的最大值放在最后,按照大小顺序排
'''
练习4：实现一个list的排序（不用sort）
思路：冒泡排序
遍历一个list，比值交换，遍历一次结束
最大值在list最后面
遍历len(list)次，排序完成
交换两个变量的写法：a,b = b,a
'''

_list = [168,180,170,169,10,88,999,23]
print _list 
_count = 0
for k in range(0,len(_list) - 1):
    for i in range(0,len(_list) - 1 -k ):
	_count += 1
        if _list[i] > _list[ i + 1 ]:
	    tmp = _list[ i + 1 ]
	    _list[ i + 1 ] = _list[i]
	    _list[i] = tmp
    print _list
print _list
print _count

'''
count是列表的长度
第一次循环 k = 0,i循环count - 1 -0(k)
i   _list[i]   _list[ i + 1 ]   _list
0   168        180		[168,180,170,169]
1   180	       170		[168,170,180,169]	 
2   180        169		[168,170,169,180]
[168,170,169,180]
第二次循环k = 1,i只需要循环count - 1 - 1(k)
0   168        170		[168,170,169,180]
1   170        169		[168,169,170,180]
2   170        180              [168,169,170,180]可以省略

'''
