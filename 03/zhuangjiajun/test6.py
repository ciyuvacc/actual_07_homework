#!/usr/bin/python
#coding:utf-8

#练习6：把一个dict的key和value反转

'''
（如果value有重复的，把多个key，放在list）
提示：判断是否list
print isinstance([1,2,3],list)
print type([1,2]) == type([])
比如{'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
期望输出 {'pc': ['teach', 'waihao', 'name'], 12: 'age', 'IT': 'job'}
'''

_dict = {'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
_d = {}
print _dict
for key,value in _dict.items():
    if value in _d:
	tmp = _d.get(value)
	if type([]) == type(tmp):
	    _d[value].append(key)
	else:
	    _d[value] = [key,tmp]
    else:
	_d[value] = key
print _d


'''
_dict = {'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
print _dict
_new = {}
for k,v in _dict.items():
    if v in _new:
	tmp = _new.get(v)
	if type([]) == type(tmp):
	    _new[v].append(k)
	else:
	    _new[v] = [tmp,k]
    else:
 	_new[v] = k
print _new
'''



#user_dict = {'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
#new_dict = {}
#for key, value in user_dict.items():
#    if value in new_dict:
#	_new_value = new_dict.get(value)
#	if type([]) == type(_new_value):
#	    new_dict[value].append(key)
#	else:
#            new_dict[value] = [_new_value, key]
#    else:
#       new_dict[value] = key
#    print '加入key:%s, value:%s' % (value, key)
#    print new_dict
#
#print new_dict
#
