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
        listStu = {}
        for user,pwd,phone in [l.split(',') for l in f]:
            listStu[user.strip()]=[pwd.strip(),phone.strip()]
        return listStu

def check_key(username):
    listStu=read_file()
    if username in listStu:
        return True
    else:
        return False

