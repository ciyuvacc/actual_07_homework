#!/usr/bin/env  python

f=file('/root/www_access_20140823.log','r')
stat_dict = {}
for line in f:
    line=line.split(' ')
    ip=line[0]
    code=line[8]
    url=line[6]
    key=(ip,url,code)
    if key not in stat_dict:
	stat_dict[key] =1
    else:
	stat_dict[key] +=1 
f.close()

stat_count_dict = {}

for key, value in stat_dict.items():
    new_key = value 
    ip, url, code = key
    new_value = [code, url, (ip, value)]
    if new_key not in stat_count_dict:
        stat_count_dict[new_key] = []
    stat_count_dict[new_key].append(new_value)

count_list = stat_count_dict.keys()

for j in range(len(count_list) - 1):
    for i in range(len(count_list) - 1):
        if count_list[i] < count_list[i + 1]:
            count_list[i], count_list[i + 1] = count_list[i + 1], count_list[i]


handle = open('rs.txt', 'w')
for count in count_list:
     for item in stat_count_dict[count]:
         handle.write(str(item) + '\n')
handle.close()
