#coding:utf-8
path1 = '/root/python/www_access_20140823.log'
path2 = '/root/python/ng_log_count.txt'
_dict = {}
count_list = []
ng_file = open(path1,'r')

for line in ng_file:
    ip = line.split(' ')[0]
    url = line.split(' ')[6]
    state= line.split(' ')[8]
    key = (state,url,ip,)
    _dict.setdefault(key,0)
    _dict[key]+=1

ng_file.close()

for _key,_value in _dict.items():
    _list = list(_key)
    _list.append(_value)
    count_list.append([_list[0],_list[1],(_list[2],_list[3])])

for i in range(len(count_list)-1):
    for j in range(len(count_list)-1-i):
        if count_list[j][2][1] < count_list[j+1][2][1]:
            count_list[j],count_list[j+1] = count_list[j+1],count_list[j]

count_log = open(path2,'w')

for count in count_list:
    _str = str(count)
    count_log.write(_str+'\n')
count_log.flush()
count_log.close()
