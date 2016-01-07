#!/usr/bin/env python
#encoding: utf-8
####方法一

iteams=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
tmp_first=''
tmp_second=''
for x in iteams:
    if tmp_first == '':
       tmp_first = x
    elif x >= tmp_first:
             tmp_second = tmp_first 
             tmp_first = x
print "The biggest number in the list are ( %d  %d )" % (tmp_first, tmp_second)  

#######方法二

iteams=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
tmp_first = iteams[0]
tmp_second = iteams[0]
for x in range(0, len(iteams)):
    if tmp_first <= iteams[x]:
             tmp_second = tmp_first 
             tmp_first = iteams[x]
print "The biggest number in the list are ( %d  %d )" % (tmp_first, tmp_second)  

