#!/usr/bin/env python

#方法一
path1 = '/opt/python/www_access_20140823.log'
#path1 = '/opt/python/www_access.log'
path2 = '/opt/python/count.log'
hd1 = open(path1,'r')
tmp_list= []
tmp_str= ''
tmp_dict = {}
for _line in hd1:
    tmp_list = [_line.split()[8],_line.split()[6], _line.split()[0]]
    tmp_str = ' '.join(tmp_list)
    tmp_dict.setdefault(tmp_str, 0)
    tmp_dict[tmp_str] += 1
hd1.close()
#print tmp_dict

'''
show_list = []  
for _key, _value in tmp_dict.items():
    show_list=_key.split()
    show_list[2]= (show_list[2], _value)
    print show_list
'''


tmp_dir = {}
for _key, _value in tmp_dict.items():
    tmp_dir.setdefault(_value, [])
    tmp_dir[_value].append(_key)
#print tmp_dir

arr_list = tmp_dir.items()
#print arr_list
for i in range(0,len(arr_list)-1):
    for j in range(0,len(arr_list)-i-1):
        if arr_list[j][0] < arr_list[j+1][0]:
            arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]
#print arr_list

tmp_list = []
hd2 = open(path2,'w')
for _list_line in arr_list:
    for _tmp_line in _list_line[1]:
         tmp_list =_tmp_line.split()
         tmp_list[2] = (tmp_list[2], _list_line[0]) 
         hd2.write(str(tmp_list)+ '\n')
hd2.close()




#方法二


#!/usr/bin/env python
import time
#path1 = '/opt/python/www_access_20140823.log'
#path1 = '/opt/python/www_access.log'
path1 = '/opt/python/hello.txt'
path2 = '/opt/python/count1.log'
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
hd1 = open(path1,'r')
_ip = ''
_status = ''
_uri = ''
_count= ''
tmp_dict = {}
for _line in hd1:
    _status = _line.split()[8]
    _uri = _line.split()[6]
    _ip = _line.split()[0]
#    print "status: %s uri: %s ip: %s" % (_status, _uri, _ip)
    if _status in tmp_dict:
        if _uri in tmp_dict[_status]:
            if _ip in tmp_dict[_status][_uri]:
#                tmp_dict[_status][_uri].setdefault(_ip, 0)
                tmp_dict[_status][_uri][_ip] += 1
            else:
                tmp_dict[_status][_uri][_ip] = 1
        else:
            tmp_dict[_status][_uri] = {}
            tmp_dict[_status][_uri][_ip] = 1
    else:
        tmp_dict[_status] = {}
        tmp_dict[_status][_uri] = {}
        tmp_dict[_status][_uri][_ip] = 1

hd1.close()
#print tmp_dict
hd2 = open(path2,'w')
tmp_list = []
tmp_str = ''
tmp_dic = {}
for _key1, _value1 in tmp_dict.items():
    for _key2, _value2 in _value1.items():
        for _key3, _value3 in _value2.items():
#            print "_key3 %s   _value3 %s" % (_key3, _value3)
#            tmp_list = [_key1, _key2, (_key3, _value3)]
#            print tmp_list 
             tmp_dic.setdefault(_value3, [])
             tmp_dic[_value3].append(_key1+' '+ _key2+' '+ _key3)
#print tmp_dic

arr_list =tmp_dic.items()
for i in range(0,len(arr_list)-1):
    for j in range(0,len(arr_list)-1-i):
        if arr_list[j][0] < arr_list [j+1][0]:
            arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]

#print arr_list

tmp_list = []
hd2 = open(path2,'w')
for _count_line in arr_list:
    for _list_line in _count_line[1]:
        tmp_list = _list_line.split()
        tmp_list[2] = (tmp_list[2], _count_line[0])
        hd2.write(str(tmp_list)+ '\n')
hd2.close()
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))





'''
不错，结果正确，最终能够想到将结果写入文件，继续加油

'''