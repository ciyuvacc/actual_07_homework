__author__ = 'XuHeng'
#coding=utf-8
from flask import Flask
from flask import render_template
from flask import Response
from flask import request,redirect
from opfile import write_file,read_file,check_key
import sys


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/userinfo')
def userinfo():
    user_list=read_file()
    print user_list
    return render_template('index.html',user_list=user_list)


@app.route('/login/', methods = ['POST'])
def GetLogin():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        user_list=read_file()
        for k,v in user_list.items():
            print k,v
            if username == k and password == v[0]:
                return redirect('/userinfo')
            else:
                return Response('帐号密码错误')
    else:
         return Response('非法提交')

@app.route('/registe/', methods = ['POST'])
def GetRegiste():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        telephone=request.form.get('telephone')
        if check_key(username):
            return Response('帐号已存在!!请更换帐号，重试')
        if write_file(username,password,telephone):
            return Response('注册成功!!!')
    else:
         return Response('非法提交')


if __name__ == '__main__':
    app.run('0.0.0.0',18080,debug=True)

