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
#from logshow import *
#from user import *
#from operation import *
import models
from functools import wraps

app = Flask(__name__)
app.secret_key=os.urandom(24)

#定义登陆的装饰器
def login_request(func):
    @wraps(func)
    def islogin(*args,**kwargs):
        if session.get('user') is None:
            return redirect('/')
        rtn = func(*args,**kwargs)
        return rtn
    return islogin

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
@login_request
def users():
    selectuser = request.form.get('query', '')
    userlist = models.get_user(selectuser)
    username = session.get('user')
    return render_template('user.html',users=userlist,username=username);

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

@app.route('/hosts/',methods=['POST','GET'])
@login_request
def hosts():
    hostname = request.form.get('query', '')
    hostlist = models.get_hostlist(hostname)
    return render_template('hosts.html',hosts=hostlist)


@app.route('/addhost/',methods=['POST'])
def addhost():
    hostname = request.form.get('hostname','')
    hostip = request.form.get('hostip','')
    hostlanip = request.form.get('hostlanip','')
    hostmemory = request.form.get('hostmemory','')
    hostdisk = request.form.get('hostdisk','')
    hostcpu = request.form.get('hostcpu','')
    hostos = request.form.get('hostos','')
    hoststatus = request.form.get('hoststatus','')
    print hostdisk
    if models.add_host(hostname,hostip,hostlanip,hostmemory,hostdisk,hostcpu,hostos,hoststatus):
        ok = True
        result = '添加主机成功'
    else:
        ok = False
        result = '添加失败'
    return json.dumps({'ok' : True, 'result': result})


@app.route('/updatehost/',methods=['POST'])
def updatehost():
    hostid = request.form.get('hostid', '')
    hostname = request.form.get('hostname', '')
    hostip = request.form.get('hostip', '')
    hostlanip = request.form.get('hostlanip', '')
    hostmemory = request.form.get('hostmemory', '')
    hostdisk = request.form.get('hostdisk', '')
    hostcpu = request.form.get('hostcpu', '')
    hostos = request.form.get('hostos', '')
    if models.updatehost(hostname,hostip,hostlanip,hostmemory,hostdisk,hostcpu,hostos,hostid):
        ok = True
        result = "更新成功"
    else:
        ok = False
        result = '更新失败'
    if ok:
        return json.dumps({'ok' : True,'result': result})
    else:
        return json.dumps({'ok': False,'result' :result})


@app.route('/deletehost/',methods=['POST'])
def deletehost():
    hostid = request.form.get('hostid','')
    hostname = request.form.get('hostname','')
    print hostid,hostname
    if models.del_host(hostid,hostname):
        ok = True
        result = "删除成功"
    else:
        ok = False
        result = "删除失败"
    if ok:
        return json.dumps({'ok' : True,'result':result})
    else:
        return json.dump({'ok': False,'result': result})


@app.route('/logs',methods=['POST'])
def logs():
    numbers = request.form.get('numbers')
    logs = models.show_log(numbers)
    return render_template('logs.html',logs=logs)



if __name__ == ('__main__'):
    app.run(debug=True)
