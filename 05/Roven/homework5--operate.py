#!/usr/bin/env python
#encoding utf-8

#### 不考虑遇优先级做法


def init_func(mystr):
  arr=list(mystr)
  if arr[0] == '-':
    arr.pop(0)
    arr[0]= '-'+arr[0] 
  tmp_list=[]
  tmpstr=''
  for a in arr:
    if a in '+-*/':
      tmp_list.append(tmpstr)
      tmp_list.append(a)
      tmpstr=''
    else:
      tmpstr=tmpstr + a
  tmp_list.append(a)
  return tmp_list
def operate(mystr): 
  tmp_list=init_func(mystr)
  tmp_count=0
  tmp_str0='+'
  num_count=0
  for a in range(0,len(tmp_list)-1,2):
    if a == 0:
      tmp_count=eval(tmp_list[a]+tmp_list[a+1]+tmp_list[a+2])
    else:
      tmp_count =eval(str(tmp_count)+tmp_list[a+1]+tmp_list[a+2])
    num_count = tmp_count
  return num_count

mystr='-10+2+2*3/4+2*3-5'
print operate(mystr)


##############  考虑优先级做法   ######################################
'''
  实现思路
arr=list(mystr)
if arr[0] == '-':
  arr.pop(0)
  arr[0]= '-'+arr[0] 
tmp_list=[]

#print arr
tmpstr=''
i=0
while i < len(arr)-1:
  if arr[i] in '+-*/':
    tmp_list.append(tmpstr)
    tmp_list.append(arr[i])
    tmpstr=''
    i += 1
  else:
    tmpstr=tmpstr + arr[i]
    i += 1
tmp_list.append(arr[i])
print tmp_list
j=3
tmp_list1=['0']
while j <len(tmp_list)-1:
  if tmp_list[j] in '*/':
    tmp_list1.append(tmp_list.pop(j-2))
    tmp_list1.append(tmp_list.pop(j-2))
    if  tmp_list[j] in '+-':
      tmp_list1.append(tmp_list.pop(j-2))
      tmp_list1.append(tmp_list.pop(j-2))

  else:
    j += 2
tmp_list1.append('+')
print tmp_list1 + tmp_list
print tmp_list
'''

def init_func1(mystr):
  arr=list(mystr)
  if arr[0] == '-':
    arr.pop(0)
    arr[0]= '-'+arr[0] 
  tmp_list=[] 
  tmpstr=''
  i=0
  while i < len(arr)-1:
    if arr[i] in '+-*/':
      tmp_list.append(tmpstr)
      tmp_list.append(arr[i])
      tmpstr=''
      i += 1
    else:
      tmpstr=tmpstr + arr[i]
      i += 1
  tmp_list.append(arr[i])
  j=3
  tmp_list1=['0']
  while j <len(tmp_list)-1:
    if tmp_list[j] in '*/':
      tmp_list1.append(tmp_list.pop(j-2))
      tmp_list1.append(tmp_list.pop(j-2))
      if  tmp_list[j] in '+-':
        tmp_list1.append(tmp_list.pop(j-2))
        tmp_list1.append(tmp_list.pop(j-2))
    else:
      j += 2
      result = tmp_list1 + ['+']+ tmp_list
  return result
def operate3(mystr): 
  tmp_list=init_func1(mystr)
  tmp_count=0
  tmp_str0='+'
  num_count=0
  for a in range(0,len(tmp_list)-1,2):
    if a == 0:
      tmp_count=eval(tmp_list[a]+tmp_list[a+1]+tmp_list[a+2])
    else:
      tmp_count =eval(str(tmp_count)+tmp_list[a+1]+tmp_list[a+2])
    num_count = tmp_count
  return num_count
mystr='10+10-22*3/2*2+1*2/2+3-5'
print init_func1(mystr)
print operate3(mystr)
