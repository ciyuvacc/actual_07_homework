#!/usr/bin/python
#coding:utf-8
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
#方法一：
max_num1=0
max_num2=0
for i in list:
    if i > max_num1 : 
        max_num1 = i
for i in list:
    if i != max_num1 and i > max_num2:
        max_num2 = i 
print '这个list中最大的两个数是%d,%d' %(max_num1,max_num2)

#方法二
max_num1 = 0
max_num2 = 0

for i in list:
    if i > max_num1:
	max_num2 = max_num1 
        max_num1 = i
    elif i > max_num2:
	max_num2 = i
print '这个list中最大的两个数是%d,%d' %(max_num1,max_num2)
    
