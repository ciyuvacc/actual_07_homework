#!/bin/env python
# -*- encoding:utf-8 -*-
# zuoye.py
# Author : Jacob.Yu
# CTime : 2016-01-16

# Task 1
# level 1
list_name = [(1,4),(5,1),(2,3)]
print list_name
print sorted(list_name,key=max)
print sorted(list_name,key=lambda x:max(x))
print sorted(list_name,cmp=lambda x,y:cmp(max(x),max(y)))

# level 2
list_name = [(1,4),(5,1),(2,3)]
print list_name
print sorted(list_name,key=lambda x:x[0] > x[1] and x[0] or x[1])

# Task 2

# read log file and get log_stat_dict
def read_log_file(log_file):
    handle = open(log_file)

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

# get log_stat_list
def change_into_list(log_dict):
    for _key in log_dict:
        _value = log_dict[_key]
        _ip,_url,_code = _key
        log_stat_list.append([_code,_url,(_ip,_value)])

# top10
def sort_top10(log_list):
    for j in range(10):
        for i in range(len(log_list) - 1):
            if log_list[i][2][1] > log_list[i + 1][2][1]:
                log_list[i],log_list[i+1] = log_list[i+1],log_list[i]
    for node in log_list[:-11:-1]:
        print node

log_file = 'www_access_20140823.log'
log_stat_dict = {}
log_stat_list = []

read_log_file(log_file)
change_into_list(log_stat_dict)
sort_top10(log_stat_list)

# Task 3