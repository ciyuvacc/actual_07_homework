#coding=utf-8
#对存储文件的读写查操作,手机号码检测
__author__ = 'XuHeng'

import os

def write_file(username,password,iphone):
    return True
    if not os.path.exists('user.txt'):
        return '数据存储异常'
    with open("user.txt", "a") as f:
            print str(username)+','+str(password)+','+str(iphone)+'\n'
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



def check_phone_num(telephone):
        phone_fix=['130','131','132','133','134','135','136','137','138','139','150','151','152','153','156','158','159','170','183','182','185','186','188','189']
        if len(telephone)<>11:
                return "手机号码为11位"
        else:
                if  telephone.isdigit():
                        if telephone[:3] in phone_fix:
                                return 'True'
                        else:
                                return "手机号码无效"
                else:
                        return "手机号码为整数，请检查"




