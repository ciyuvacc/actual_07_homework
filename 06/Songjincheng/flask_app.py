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
            return redirect('/user/')
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
        pwd = request.form.get('pwd')
        email = request.form.get('email')
        IPhone = request.form.get('IPhone')
        with open('name.txt','a') as handle:
            handle.write('%s,%s,%s,%s' % (name, pwd, email, IPhone))
    files = filename('name.txt')
    return render_template('user.html', file=files)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#在注册页面输入后，提交，写不到文件里，但POST还没有报错， 请老师指点
