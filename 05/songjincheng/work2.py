#!/usr/bin/env python
#-*- coding:utf-8 -*-


dic_data = {}
list_data = []

def logfile(name):
    with open(name,'r') as handle:
        while True:
            log = handle.readline()
            if '' == log:
                break
            logfile = log.split()
            ip = logfile[0]
            url = logfile[6]
            status = logfile[8]
            all = (ip, url, status) 
            dic_data.setdefault(all, 0)
            dic_data[all] += 1
    return dic_data

def datalist(key):
    for _key in key:
        if '' == _key:
            break
        value = dic_data[_key]
        ip, url, status = _key
        list_data.append([status, url,(ip,value)])
    for j in range(10):
        for i in range(len(list_data) - 1):
            if list_data[i][2][1] > list_data[i + 1][2][1]:
                list_data[i],list_data[i + 1] = list_data[i + 1],list_data[i]
    for i in list_data[:-11:-1]:
        print i

if __name__ == '__main__':
    datalist(logfile('/srv/salt/www_access_20140823.log'))

 
     
'''
ok,  没有问题，将不同功能进行拆分
如果我有时候想要获取TOP 10， 有时候想要获取Top 20，应该怎么做呢？

建议将
dic_data = {}
list_data = []
定义到函数内，缩小名字空间范围
'''
