#!/usr/bin/env python
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
