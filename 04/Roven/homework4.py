#!/usr/bin/env python
path1 = '/opt/python/www_access_20140823.log'
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
show_list = []  
for _key, _value in tmp_dict.items():
    show_list=_key.split()
    show_list[2]= (show_list[2], _value)
    print show_list

