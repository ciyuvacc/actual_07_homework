#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import  os
import  json
import math
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
#from logshow import *
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

@app.route('/login/',methods=['GET','POST'])
def login():
    method = request.args if request.method == 'GET' else request.form
    user = models.User(method)
    if user.auth_user():
        session['user'] = {'username':user.username}
     	return redirect('/users')
    if user.username != "" and user.exist_user():
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
    method = request.args if request.method == 'GET' else request.form
    selectuser = method.get('query', '')
    total = models.User.fetch_all(selectuser)
    pagesize = method.get('pageSize',10)
    pagenum = method.get('pageNum',1)
    pagesize = int(pagesize) if str(pagesize).isdigit()\
                else 10
    pagesize = 10 if pagesize <= 5 or pagesize >= 20 \
                else pagesize
    max_page_num = int(math.ceil(total * 1.0 / pagesize))

    pagenum = int(pagenum) if str(pagenum).isdigit() else 1
    # 如果页数小于1 或者大于最大的页数就把页数设置成1 否则就是正常页数
    pagenum = 1 if pagenum < 1 or pagenum > max_page_num else pagenum
    #设置从那条数据开始读取 开始数 = 页数 - 1 乘以 页面展示数
    offset = (pagenum - 1 ) * pagesize
    # 显示的开始页表示显示当前页和之前的两页 如果开始页小于1 就显示第一页
    start_page_num = pagenum - 2
    start_page_num = 1 if start_page_num < 1 else start_page_num
    # 可现实的最大页数 如果可显示的最大页数大于最大页数则只显示到最大页数
    end_page_num = start_page_num + 5
    end_page_num = end_page_num if end_page_num <= max_page_num else max_page_num

    userlist = models.User.all_users(selectuser,offset,pagesize)
    return render_template('user.html',users=userlist,query=selectuser,\
                           start_page_num=start_page_num,end_page_num=end_page_num,\
                           pagenum=pagenum,pagesize=pagesize,max_page_num=max_page_num);

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
    method = request.args if request.method == 'GET' else request.form
    user = models.User(method)
    if user.exist_user():
        user.add_user()
        ok = True
        result = "添加成功"
        return json.dumps({'ok' : True,'result':result})
    else:
        ok = False
        result = "添加失败"
        return json.dumps({'ok': False,'result':result})


@app.route('/updateuser/',methods=['POST'])
def updateuser():
    method = request.args if request.method == 'GET' else request.form
    user = models.User(method)
    if user.modify_user():
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
    method = request.args if request.method == 'GET' else request.form
    user = models.User(method)
    if user.delete_user():
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
    method = request.args if request.method == 'GET' else request.form
    hostname = method.get('query', '')
    print method.get('pageNum')
    print method.get('pageSize')
    total = models.Host.fetch_all_host(hostname)
    pagesize = method.get('pageSize',10)
    pagenum = method.get('pageNum',1)
    pagesize = int(pagesize) if str(pagesize).isdigit()\
                else 10
    pagesize = 10 if pagesize <= 5 or pagesize >= 20 \
                else pagesize
    max_page_num = int(math.ceil(total * 1.0 / pagesize))

    pagenum = int(pagenum) if str(pagenum).isdigit() else 1
    # 如果页数小于1 或者大于最大的页数就把页数设置成1 否则就是正常页数
    pagenum = 1 if pagenum < 1 or pagenum > max_page_num else pagenum
    #设置从那条数据开始读取 开始数 = 页数 - 1 乘以 页面展示数
    offset = (pagenum - 1 ) * pagesize
    # 显示的开始页表示显示当前页和之前的两页 如果开始页小于1 就显示第一页
    start_page_num = pagenum - 2
    start_page_num = 1 if start_page_num < 1 else start_page_num
    # 可现实的最大页数 如果可显示的最大页数大于最大页数则只显示到最大页数
    end_page_num = start_page_num + 5
    end_page_num = end_page_num if end_page_num <= max_page_num else max_page_num
    hostlist = models.Host.get_hostlist(hostname,pagesize,offset)
    return render_template('hosts.html',hosts=hostlist,query=hostname,\
                           start_page_num=start_page_num,end_page_num=end_page_num,\
                           pagenum=pagenum,pagesize=pagesize,max_page_num=max_page_num)


@app.route('/addhost/',methods=['POST'])
def addhost():
    method = request.args if request.method == 'GET' else request.form
    host = models.Host(method)
    if host.add_host():
        ok = True
        result = '添加主机成功'
    else:
        ok = False
        result = '添加失败'
    return json.dumps({'ok' : True, 'result': result})


@app.route('/updatehost/',methods=['POST'])
def updatehost():
    host = models.Host(request.form)
    if host.updatehost():
        ok = True
        result = "更新主机信息成功"
    else:
        ok = False
        result = '主机信息无变化'
    if ok:
        return json.dumps({'ok' : True,'result': result})
    else:
        return json.dumps({'ok': False,'result' :result})


@app.route('/deletehost/',methods=['POST'])
def deletehost():
    host = models.Host(request.form)
    if host.del_host():
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
