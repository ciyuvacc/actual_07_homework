#encoding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import models

app = Flask(__name__)
#默认登陆页面
@app.route('/')
def index():
    return render_template('index.html')

#用户登陆验证
@app.route('/login/',methods=["POST"])
def login():
    username =  request.form.get('username','')
    password =  request.form.get('password','')
    if models.validate_user_login(username,password):
        print username,password
        with open('tmp_user','w') as txt:
            print >> txt,username
            txt.close()
        return render_template('/index2.html',loginusername = username)
    else:
        return render_template('/index.html',loginerror = '登陆失败，用户名或密码错误', loginusername = username, loginpassword = password)
#注册、注册验证
@app.route('/register/',methods=["POST"])
def register():
    username =  request.form.get('username','')
    password =  request.form.get('password','')
    age = request.form.get('age','')
    address = request.form.get('address','')
    ok,info =  models.validate_user_register(username,password,age,address)
    if ok:
        models.add_user(username,password,age,address)
        validate = models.validate_user_login(username,password)
        if validate:
            info = '恭喜您，注册成功'
        else:
	    info = '注册失败了'
        return render_template('/index.html',registerok=ok, registerinfo=info)
    else:
        return render_template('/index.html',registerok=ok, registerinfo=info,usernameinfo = username,passwordinfo = password,ageinfo = age,addressinof = address)
#删除用户功能
@app.route('/deluser',methods=["POST"])
def deluser():
    #deluser = name=request.args.get('userid','')
    deluser =request.form.get('userid','')
    print deluser
    ok =  models.del_user(deluser)
    if ok:
        return "true"
    else:
        return "false"
@app.route('/modeuser',methods=["POST"])
#修改用户信息功能
def modeuser():
    print 'ok!!'
    modeuser = request.form.get('userid','')
    modeage = request.form.get('modeage','')
    modeaddress = request.form.get('modeaddress','')
    ok = models.mode_user(modeuser,modeage,modeaddress)
    print ok
    if ok:
        return 'true'
    else:
        return "false"

#修改登陆用户密码
@app.route('/userpwd',methods=["post"])
def userpwd():
    username = open('tmp_user','r').read()
    user_name = request.form.get('username','')
    str(user_name)
    username = username.replace('\n','')
    setusername = request.form.get('setusername','')
    setpassword = request.form.get('setpassword','')
    print setusername,setpassword
    if setpassword != '' and setusername != '':
        ok = models.mode_setpassword(setusername,setpassword)
        if ok:
            info = "密码更改成功"
        else:
            info =  "失败，密码应该6到32位的字符串"
        return render_template('/setpwd.html',setusername=username,info = info,setpassword = setpassword)
    if user_name ==  username:
        return render_template('/setpwd.html',setusername=username)
    else:
        return 'no'
#nginx日志页面
@app.route('/logs',methods=['POST'] )    
def logs():
    bb = ''
    try:
        n = request.form.get('count')
        n = int(n)
    except:
        n = 0
        bb = "请输入一个正确的数字！"
    if type(n) == type(1):
        logs = models.get_logs(n)
    else:
        logs = models.get_logs(10)
    return render_template('/logs.html', logs=logs, bbinfo = bb)
#用户信息页面
@app.route('/users',methods=['post'])
def users():
    users = models.get_users()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
