#!/usr/bin/python
#coding:utf-8
'''
照着视频按照师讲的敲了一遍···
'''
'''
logtext = '10.35.1.82 - - [23/Aug/2014:00:07:12 +0800] "GET /data/uploads/2014/0429/10/535f13f4a13da.jpg HTTP/1.0" 200 \ "-" "-" "-"'

log_list = logtext.split(' ')
ip = log_list[0]
url = log_list[6]
code = log_list[8]

print ip,url,code
'''
stat_dict = {}
handle = open('www_access_20140823.log','r')

for line in handle:
    line_list = line.split(' ')
    ip = line_list[0]
    url = line_list[6]
    code = line_list[8]

    key=(ip,url,code)
    if key not in stat_dict:
	stat_dict[key] = 1
    else:
	stat_dict[key] = stat_dict[key] + 1

handle.close()
stat_count_dict = {}
for key,value in stat_dict.items():
    new_key = value
    ip,url,code = key
    new_value = [code,url,(ip,value)]
    if new_key not in stat_count_dict:
        stat_count_dict[new_key] = []
    stat_count_dict[new_key].append(new_value)
print stat_count_dict.keys()

count_list = stat_count_dict.keys()

for j in range(len(count_list) - 1):
    for i in range(len(count_list) - 1):
	if count_list[i] < count_list[i + 1]:
	    count_list[i],count_list[i + 1] = count_list[i + 1],count_list[i]

print count_list
index = 0
top = 10
handle = open('rs.txt','w')
for  count in count_list:
    for item in stat_count_dict[count]:
	handle.write(str(item) + '\n')
handle.close()
