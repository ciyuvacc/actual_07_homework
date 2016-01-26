#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask
from flask import render_template   
from flask import request
from flask import redirect
import models

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=["POST"])
def login():
    username = request.form.get('username','')
    password = request.form.get('password','')
    if models.validate_user_login(username,password):
        return redirect('/users/')
    else:
	return render_template('index.html', \
			loginerror='用户名或密码错误', \
			loginusername=username, \
			loginpassword=password)
						
@app.route('/register/', methods=["POST"])
def register():
    username = request.form.get('username','')
    password = request.form.get('password','')
    age = request.form.get('age','')
    address = request.form.get('address','')
    if models.query_user(username):
        return render_template('index.html', \
                        register_error='注册失败，用户名重复', \
                        username=username)
    else:

        if models.validate_user_add(username,password,age,address):
            return '注册成功, %s ' % models.query_user(username)
        else:
            return render_template('index.html')

@app.route('/users/')		
def users():
    return '登录成功'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
