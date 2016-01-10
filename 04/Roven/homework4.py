#!/usr/bin/env python
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



