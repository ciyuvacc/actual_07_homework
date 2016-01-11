#!/usr/bin/python
#coding:utf-8

'''
练习9:用户输入员工名字和id，名字和id之间用:分隔
多个用户 用逗号分隔
最终输入所有用户对应id的信息
比如用户输入user1:119,user2:112,user3:113
最终输出[('user2', '112'), ('user3', '113'), ('user1', '119')]
'''

_user = raw_input('请输入员工信息： ')
_list = []
for i in _user.split(','):
    _list.append(tuple(i.split(':')))
print _list
