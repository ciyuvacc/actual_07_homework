#coding=utf-8
#作业：LIST最大的2个值
#列表1：[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
list_a = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_1 = 0
max_2 = 0
for i in list_a:
    if i > max_2:
        max_1 = max_2
        max_2 = i
print 'num %s,%s' % (max_1,max_2)

#列表1：[1,2,3,2,12,3,1,65543,3,21,11111111,99999,4111,22,3333,444,111,888888,8888,166667,68555,45,33,45]
# 列表2：[1,2,3,'a',2,12,3,1,65543,3,21,'b',[1,2],2,(2,3),11111111,99999,4111,22,3333,444,111,888888,8888,166667,68555,45,33,45]
list_b = [1,2,3,'a',2,12,3,1,65543,3,21,'b',[1,2],2,(2,3),11111111,99999,4111,22,3333,444,111,888888,8888,166667,68555,45,33,45]
max_a = 0
max_b= 0
for i in list_b:
    if type(i) != type(1):
        continue
    if i > max_a :
        if i >max_b:
             max_a = max_b
             max_b = i
        else:
            max_a = i
print 'num %s,%s' % (max_a,max_b)


#! /usr/bin/python
# Filename : table_9x9.py
# Author : Jesse
# Date : 2011/08/13 21:50

print '\n9x9 Table\n'

for i in range(1, 10) :
    for j in range(1, i+1) :
        print j, 'x', i, '=', j*i, '\t',
        # print '%d x %d = %d\t' %(j, i, j*i),
    print '\n'

print '\nDone!'



