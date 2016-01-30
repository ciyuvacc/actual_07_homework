#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


from flask import Flask,request
from flask import render_template,redirect
import models


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',methods=['POST'])
def login():
    username =  request.form.get('username','')
    password = request.form.get('password','')
    if models.validate_user_login(username,password):
      return redirect('/users/')
    else:
      return render_template('index.html',\
                          loginerror='用户名或者密码错误',\
                          loginusername=username,\
                          loginpassword=password)



#验证用户登录的用户名和密码
@app.route('/register/',methods=['POST'])
def register():
  username = request.form.get('username','')
  password = request.form.get('password','')
  age = request.form.get('age','')
  address = request.form.get('address','')

 
  if username == '':
    tip = "用户名不能为空！"
    return render_template('index.html',name_null=tip)

  if password == '':
    tip = "密码不能为空！"
    return render_template('index.html',password_null=tip)

  if not models.isNum(age):
    tip = "年龄必须是数字！"
    return render_template('index.html',age_num=tip)

  if  models.valid_user_name(username):
    tip = '用户名已存在，请重新输入用户名'
    return render_template('index.html',ValidNameInfo=tip)
  else:
    ok,info = models.valid_user_register(username,password,age,address)
    if ok:
      models.valid_user_register(username,password,age,address)
      info = '注册成功'
    return render_template('index.html',registerok=ok,registerinfo=info)
  
#获取用户的信息
@app.route('/users/')
def users():
    users = models.get_users()
    return render_template('users.html', users=users)



#更新用户信息：
@app.route('/update/',methods=['POST'])

def update():
  username = request.form.get('username','')
  password = request.form.get('password','')
  age = request.form.get('age','')
  address = request.form.get('address','')
  
  ok,result = modes.update_user(name,password,age,address)
  
  if ok:
      modes.update_user(name,password,age,address)
      info = '更新用户信息成功'
      return render_template('index.html',update_user_ok=ok,update_userinfo=info)



#删除用户信息
@app.route('/delete/',methods=['POST'])
def delete():
  username = request.form.get('username','')
  if models.delete_user(username):
    return redirect('/users/')
  else:
    return render_template('index.html',deluser_error='删除失败',loginusername=username)





if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8888,debug=True)

