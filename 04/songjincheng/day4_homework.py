#!/usr/bin/env python
#-*- coding:utf-8 -*-

#status, url, ip
#['404', '/images/cursor zoom.cur', ('118.112.143.148', 674)]
dic = {}
dic_list = []
f = open('www_access_20140823.log','r+')
for i in f.read().split('\n'):
    logfile = i.split()
    status = logfile[8]
    url = logfile[6]
    ip = logfile[0]
    dic[ip] = dic.setdefault(ip,1) + 1
    for ip,count in dic.items():
        dic_list.append([status,url,(ip,count,)])
    for i in sorted(dic_list, key=lambda cmp:cmp[2][1],reverse=True)[0:10]:
        print i 

      
    

'''
不错，想法是对的，结果正确不太正确，注意缩进12-18行
已经自己学习使用新的知识点完成作业，相当努力，继续加油

可以改进的地方
1. read().split('\n')建议使用readlines或者readline，后者用文件对象
原因：a.read是将文件内容全部读到内存中，占用内存较多
b. win和*nix中换行符不一致，readline和readlines做了兼容处理

'''