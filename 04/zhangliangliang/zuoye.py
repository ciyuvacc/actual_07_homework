#!/usr/bin/env python
logfile = open('www_access_20140823.log','r')
stat_dict = {}
for line in logfile:
    line_list = line.split(' ')
    ip = line_list[0]
    url = line_list[6]
    code = line_list[8]
    key = (ip,url,code)
    stat_dict.setdefault(key,0)
    stat_dict[key] += 1

logfile.close()

stat_count_dict = {}
for key,value in stat_dict.items():
    new_key = value
    ip,url,code = key
    new_value = [code,url,(ip,value)]
    stat_count_dict[new_key] = new_value

_count = 0
_top = 10
stat_count_list = stat_count_dict.keys()
stat_count_list.sort(reverse=True)
for i in stat_count_list:
    _count += 1
    print stat_count_dict[i]
    if _count == _top:
        break
