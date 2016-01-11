#!/usr/bin/python
#coding:utf-8

_userlist = [('woniu','123456'),('pc','654321'),('pc2','123456789')]
_username = 'pc'
_userpwd = ''

for i in _userlist:
    if i[0] == _username:
	_userpwd = i[1]
	break
print '%s,%s' %(_username,_userpwd)
