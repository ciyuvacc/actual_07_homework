#!/usr/bin/env python
#coding:utf-8
# 分析nginx日志，打印前N行

import sys

# 统计数据
def Log_fenxi(log_name):
    try:
        log_file = open(log_name)
    except IOError:
        print "\n\tNo such file or directory: '%s'" % log_name
        exit()
    log_stat_dict = {}
    global log_stat_list
    log_stat_list = []
    for _line in log_file:
        _line_nodes = _line.split()
        _ip,_url,_code = _line_nodes[0],_line_nodes[6],_line_nodes[8]
        _key = (_ip,_url,_code)
        log_stat_dict.setdefault(_key,0)
        log_stat_dict[_key] += 1
    log_file.close()
    for _key,_value in log_stat_dict.items():
        _ip,_url,_code = _key
        log_stat_list.append([_code,(_ip,_value),_url])

# 冒泡排序，获取top N
def top_sort(n):
    for j in range(n):
        for i in range(len(log_stat_list) - 1):
            if log_stat_list[i][1][1] > log_stat_list[i+1][1][1]:
                log_stat_list[i],log_stat_list[i+1] = log_stat_list[i+1],log_stat_list[i]
    for top in log_stat_list[:-(n+1):-1]:
        print top

# 获取命令行指定的日志文件名,打印N行
try:
    top_n = int(sys.argv[1])
    filename = sys.argv[2]
    Log_fenxi(filename)
    print "========== 访问TOP %s ：状态，IP，访问次数，URL ==========" % top_n
    top_sort(top_n)
except:
    print "\nUsage: %s <Number> <File name>" % sys.argv[0]

