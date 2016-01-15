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
