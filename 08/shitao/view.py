#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import  os
import  json
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from user import *
import models

app = Flask(__name__)
app.secret_key=os.urandom(24)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if models.auth_user(username,password):
        session['user'] = {'username':username}
     	return redirect('/users')
    if username != "" and models.exist_user(username):
        return render_template('index.html',usererror="用户不存在")
    else:
	    return render_template('index.html',loginerror="用户名或密码错误")

#退出登录
@app.route('/logout/')
def logout():
    session.pop('user','None')
    return redirect('/')

@app.route('/users/',methods=['GET','POST'])
def users():
    selectuser = request.form.get('selectuser', '')
    userlist = models.get_user(selectuser)
    if session.get('user') is None:
           return redirect('/')
    username = session.get('user')
    return render_template('user_list.html',users=userlist,username=username);

@app.route('/register/',methods=['POST'])
def register():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    email = request.form.get('email', '')
    if models.exist_user(username, email):
        models.add_user(username, password, email)
        return redirect('/')
    else:
        return render_template('index.html', registererror="用户或邮箱已被注册")

@app.route('/createuser/')
def createUser():
    return render_template('createuser.html')

@app.route('/adduser/',methods=['POST'])
def adduser():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    email = request.form.get('email', '')
    if models.exist_user(username,email):
        models.add_user(username,password,email)
        ok = True
        result = "添加成功"
        return json.dumps({'ok' : True,'result':result})
    else:
        ok = False
        result = "添加失败"
        return json.dumps({'ok': False,'result':result})

@app.route('/updateuser/',methods=['POST'])
def updateuser():
    password = request.form.get('password', '')
    email = request.form.get('email', '')
    id = request.form.get('id', '')
    if models.modify_user(password,email,id):
        ok = True
        result = "ok"
    else:
        ok = False
        result = 'error'
    if ok:
        return json.dumps({'ok' : True})
    else:
        return json.dumps({'ok': False,'result' :result})

@app.route('/deleteuser/',methods=['GET','POST'])
def deleteuser():
    username = request.form.get('username', '')
    print username
    if models.delete_user(username):
        ok = True
        result = "删除成功"
    else:
        ok = False
        result = '删除失败'
    if ok:
        return json.dumps({'ok' : True, 'result': result})
    else:
        return json.dumps({'ok': False,'result' :result})




@app.route('/logs',methods=['POST'])
def logs():
    numbers = request.form.get('numbers')
    logs = models.show_log(numbers)
    return render_template('logs.html',logs=logs)
