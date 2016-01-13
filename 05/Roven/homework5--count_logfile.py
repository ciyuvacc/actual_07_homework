#!/usr/bin/env python

#方法一
'''
1.以status 接口  ip为key 统计出相应的count值 并生成dict
   {'status uri ip': count}
2.将dict反转过来
   {count: ['status1 uri1 ip1','status2 uri2 ip2']}
3.转化成list，并按照count排序  以便后续写入文件
   [(count: ['status1 uri1 ip1','status2 uri2 ip2'])]
4.以轮询方式将上面的list按照格式写入文件（有顺序）

'''
#!/usr/bin/env python
import time
infile = '/opt/python/www_access_20140823.log'
#infile = '/opt/python/www_access.log'
#path1 = '/opt/python/hello.txt'
outfile = '/opt/python/count.log'
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def read_file(infile):
    hd1 = open(infile,'r')
    tmp_list= []
    tmp_str= ''
    tmp_dict = {}
    for _line in hd1:
        tmp_list = [_line.split()[8],_line.split()[6], _line.split()[0]]
        tmp_str = ' '.join(tmp_list)
        tmp_dict.setdefault(tmp_str, 0)
        tmp_dict[tmp_str] += 1
    hd1.close()
    return tmp_dict

def index_count(tmp_dict):
    tmp_dir = {}
    for _key, _value in tmp_dict.items():
        tmp_dir.setdefault(_value, [])
        tmp_dir[_value].append(_key)
    return tmp_dir

def turn_list(tmp_dir):
    arr_list = tmp_dir.items()
    for i in range(0,len(arr_list)-1):
        for j in range(0,len(arr_list)-i-1):
            if arr_list[j][0] < arr_list[j+1][0]:
                arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]
    return arr_list

def write_file(arr_list):
    tmp_list = []
    hd2 = open(outfile,'w')
    for _list_line in arr_list:
        for _tmp_line in _list_line[1]:
            tmp_list =_tmp_line.split()
            tmp_list[2] = (tmp_list[2], _list_line[0]) 
            hd2.write(str(tmp_list)+ '\n')
    hd2.close()
    print "write file order by count"

tmp_dict=read_file(infile)
tmp_dir=index_count(tmp_dict)
arr_list=turn_list(tmp_dir)
write_file(arr_list)

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))




#方法二
'''
1.遍历文件按照status为key生成一个dict 在其对应的value中在以[uri]为key1生成一个dict1  其对应的value1是一个 以ip为key2 count为value2的一个dict，对应关系如下
   {status1：{uri1：{ip：count}}}
2.嵌套循环遍历dict，生成一个以count为key的dict，便于排序
   {count: ['status1 uri1 ip1','status2 uri2 ip2']}
3.转化成list，并按照count排序  以便后续写入文件
   [(count: ['status1 uri1 ip1','status2 uri2 ip2'])]
4.以轮询方式将上面的list按照格式写入文件（有顺序）

'''
#!/usr/bin/env python
import time
infile = '/opt/python/www_access_20140823.log'
#infile = '/opt/python/www_access.log'
#path1 = '/opt/python/hello.txt'
outfile = '/opt/python/count1.log'
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def read_file(infile):
    hd1 = open(infile,'r')
    _ip = ''
    _status = ''
    _uri = ''
    _count= ''
    tmp_dict = {}
    for _line in hd1:
        _status = _line.split()[8]
        _uri = _line.split()[6]
        _ip = _line.split()[0]
#        print "status: %s uri: %s ip: %s" % (_status, _uri, _ip)
        if _status in tmp_dict:
            if _uri in tmp_dict[_status]:
                if _ip in tmp_dict[_status][_uri]:
#                    tmp_dict[_status][_uri].setdefault(_ip, 0)
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
    return tmp_dict
def index_count(tmp_dict):
    tmp_list = []
    tmp_str = ''
    tmp_dic = {}
    for _key1, _value1 in tmp_dict.items():
        for _key2, _value2 in _value1.items():
            for _key3, _value3 in _value2.items():
#                print "_key3 %s   _value3 %s" % (_key3, _value3)
#                tmp_list = [_key1, _key2, (_key3, _value3)]
#                print tmp_list 
                 tmp_dic.setdefault(_value3, [])
                 tmp_dic[_value3].append(_key1+' '+ _key2+' '+ _key3)
    return tmp_dic

def turn_list(tmp_dic):
    arr_list =tmp_dic.items()
    for i in range(0,len(arr_list)-1):
        for j in range(0,len(arr_list)-1-i):
            if arr_list[j][0] < arr_list [j+1][0]:
                arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]

    return arr_list
def write_file(arr_list):
    tmp_list = []
    hd2 = open(outfile,'w')
    for _count_line in arr_list:
        for _list_line in _count_line[1]:
            tmp_list = _list_line.split()
            tmp_list[2] = (tmp_list[2], _count_line[0])
            hd2.write(str(tmp_list)+ '\n')
    hd2.close()
    print "write file order by count"

tmp_dict=read_file(infile)
tmp_dic=index_count(tmp_dict)
arr_list=turn_list(tmp_dic)
write_file(arr_list)

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

