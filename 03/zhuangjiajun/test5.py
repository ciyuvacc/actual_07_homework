#!/usr/bin/python
#coding:utf-8

#练习5：实现update功能
user_dict = {'pc':'pc_pwd','woniu':'woniu_pwd','xg':'xg_pwd'}
user_dict.update({}.fromkeys(['woniu','xg','zhuangjiajun'],'fuck'))
print user_dict
