#coding=utf-8
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from logshow import *
from user import *
from operation import *

app = Flask(__name__)
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth_login',methods=['get','post'])
	        
def auth_login():
    _dict = {}
    if request.method == 'GET':
        name = request.args.get('username')
        password = request.args.get('password')
    else:
        name = request.form.get('username')
        password = request.form.get('password')
    with open('user.txt','r') as f:
        for line in f:
	    line = line.split()
	    _dict[line[0]] = line[1]
        if name in _dict and _dict[name] == password:
            return redirect('/users')
    	else:
	    return render_template('login.html',error=u"用户名或密码错误")

@app.route('/regedit/',methods=['get','post'])
def regedit():
    return render_template('regedit.html')

@app.route('/regedit2/',methods=['get','post'])
def regedit2():
    _userlist = {}
    if request.method == 'POST':
        name = request.form.get(u'username')
        password = request.form.get('password')
        email = request.form.get('email')
    with open('user.txt','a+') as f:
        for line in f:
            line = line.split()
            _userlist[line[0]] = line[1]
        if name in _userlist:
            return render_template('regedit.html',fail=u'用户已存在')
        else:
            f.write(' '.join((name,password,email+'\n')))
            return redirect('/')

@app.route('/users')
def users():
    userlist = get_user('user.txt')    
    return render_template('user_list.html',users=userlist);

@app.route('/result/',methods=['get','post'])
def result():
    userlist = get_user('user.txt')    
    if request.method == "POST":
        numbers = request.form.get('numbers')
        arr = priority2(numbers)
	result = opera(arr)
        return render_template('user_list.html',result=result,users=userlist)


if __name__ == ('__main__'):
    app.run(host='192.168.59.128',debug=True)
