#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request, redirect, render_template

app = Flask(__name__)

def filename(name):
    data_list = []
    with open(name,'r') as handle:
        while True:
            filename = handle.readline()
            if '' == filename:
                break
            name_list = filename.split()
            data_list.append(name_list)
    return data_list

def file_name(name):
    data_name = {}
    with open(name,'r') as handle:
        while True:
            filename = handle.readline()
            if '' == filename:
                break
            name = filename.split()
            username = name[0]
            password = name[1]
            data_name[username] = password
    return data_name


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
    data = file_name('name.txt')    
    for key, value in data.items():
        if username == key and password == value:
            files = filename('name.txt')
            return render_template('user.html', file=files)
    return render_template('login.html')

@app.route('/user/',methods=['GET','POST'])
def user():
    if request.method == 'GET':
        name = request.args.get('name')
        pwd = request.args.get('password')
        email = request.args.get('email')
        IPhone = request.args.get('IPhone')
    else:
        name = request.form.get('name')
        pwd = request.form.get('password')
        email = request.form.get('email')
        IPhone = request.form.get('IPhone')
        with open('name.txt','a') as handle:
            handle.write('%s %s %s %s\n' % (name, pwd, email, IPhone))
    return redirect('/successful/')


@app.route('/successful/')
def successful():
    return "注册成功"
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

'''
#1,错误是注册时候，密码为None,以及注册后，跳转页面问题，已改正代码。

不错，一定要跟着节奏走, 哪怕写代码有问题，但是慢慢改就回有进步, 继续加油

问题：
1. 注册后密码显示为None,  原因见57行, 看看html提交的密码name是什么?
2, 登陆成功应该跳转到用户列表的页面，但是现在在44行重定向到/user/上，应该使用render_template('user.html', file=data), file是你在user.html需要使用的，但是file是python的内建关键函数, 避开使用他
'''
