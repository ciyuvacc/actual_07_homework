#!/usr/bin/env python
#coding:utf8
#修改：比较大小替换成函数

#日志转换成字典
stat_dict = {}
log = open('/data/log/www_access_20140823.log','r')

for line in log:
  log_list = line.split(' ')
  ip = log_list[0]
  url = log_list[6]
  status = log_list[8]

  key = (ip,url,status)
  stat_dict.setdefault(key,1)
  stat_dict[key] += 1
log.close()

#key和value反转，计算访问信息出现的次数
#dict=>list
stat_count_dict = {}

for key,value in stat_dict.items():

  new_key = value
  new_value = [status,url,(ip,value)]
  if new_key not in stat_count_dict:
    stat_count_dict[new_key] = []
  stat_count_dict[new_key].append(new_value)

count_list =  stat_count_dict.keys()
#对访问信息的次数进行排序
def paixu(m,n):
  return m < n
  
for j in range(len(count_list)-1):
  for i in range(len(count_list)-1):
    paixu(count_list[i],count_list[i+1])
    count_list[i],count_list[i+1] = count_list[i+1],count_list[i]


#把输出写入到文件
handle = open('result.txt','w')
for count in count_list:
  for item in stat_count_dict[count]:
    handle.write(str(item) + '\n')  

'''
注意:
line 39行是一个if条件的判断，少了if语句
line 44行打开的文件，注意关闭

我们想想，函数的定义主要是输入，输出不同，对于不同的输入可能有不能的输出，但是对于处理过程是相同的
在这里你可以考虑，如果要统计多个不同的文件，你需要改动什么东西？如果不同的文件对应到不同的输出文件中，又需要改动什么东西
按这样是不是就只有输入的文件和输入的文件路径不一样呢？如果我需要你找到数量最多的TOP N个时，你有需要调整什么呢？


#对访问信息的次数进行排序
def paixu(m,n):
  return m < n

def log_analysis(src, dst, n=-1):
  stat_dict = {}
  log = open(src,'r')

  for line in log:
    log_list = line.split(' ')
    ip = log_list[0]
    url = log_list[6]
    status = log_list[8]

    key = (ip,url,status)
    stat_dict.setdefault(key,1)
    stat_dict[key] += 1
  log.close()

  #key和value反转，计算访问信息出现的次数
  #dict=>list
  stat_count_dict = {}

  for key,value in stat_dict.items():

    new_key = value
    new_value = [status,url,(ip,value)]
    if new_key not in stat_count_dict:
      stat_count_dict[new_key] = []
    stat_count_dict[new_key].append(new_value)

  count_list =  stat_count_dict.keys()

  for j in range(len(count_list)-1):
    for i in range(len(count_list)-1):
      if paixu(count_list[i],count_list[i+1]):
        count_list[i],count_list[i+1] = count_list[i+1],count_list[i]

  #把输出写入到文件
  handle = open(dst,'w')
  _cnt = 0
  for count in count_list:
    for item in stat_count_dict[count]:
      handle.write(str(item) + '\n')
      _cnt += 1
      if n != -1 && _cnt >= n:
        break

  handle.close() 

log_analysis('/data/log/www_access_20140823.log', 'result.txt')
'''