__author__ = 'XuHeng'
#coding=utf-8
#对存储文件的读写查操作

import os

def write_file(username,password,iphone):
    if not os.path.exists('user.txt'):
        return '数据存储异常'
    with open("user.txt", "a") as f:
            f.writelines(str(username)+','+str(password)+','+str(iphone)+'\n')
            f.flush()
            return True

def read_file():
    if not os.path.exists('user.txt'):
        return '数据存储异常'
    with open("user.txt", "r") as f:
        user_dict = {}
        for user,pwd,phone in [l.split(',') for l in f]:
            user_dict[user.strip()]=[pwd.strip(),phone.strip()]
        return user_dict

def check_key(username):
    user_dict=read_file()
    if username in user_dict:
        return True
    else:
        return False

