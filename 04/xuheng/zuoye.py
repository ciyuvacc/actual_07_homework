#!/bin/env python
# -*- encoding:utf-8 -*-


log_stat_dict = {}
# 读取文件
handle = open('www_access_20140823.log')

while True:
    _line = handle.readline()
    if '' == _line:
        break
    _log_nodes = _line.split()
    _ip = _log_nodes[0]
    _url = _log_nodes[6]
    _code = _log_nodes[8]
    
    _key = (_ip,_url,_code)
    log_stat_dict.setdefault(_key,0)
    log_stat_dict[_key] += 1

handle.close()

#print log_stat_dict

log_stat_list = []
for _key in log_stat_dict:
    _value = log_stat_dict[_key]
    _ip,_url,_code = _key
    log_stat_list.append([_code,_url,(_ip,_value)])

#print log_stat_list

# top10
for j in range(10):
    for i in range(len(log_stat_list) - 1):
        if log_stat_list[i][2][1] > log_stat_list[i + 1][2][1]:
            log_stat_list[i],log_stat_list[i+1] = log_stat_list[i+1],log_stat_list[i]

for node in log_stat_list[:-11:-1]:
    print node