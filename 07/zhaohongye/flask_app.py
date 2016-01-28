#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from models import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login/', methods = ['GET','POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	if validate_user_login(username,password) == True:
		return redirect('login_ok')
	else:
		return render_template('index.html', message='Bad username or password')

@app.route('/login_ok/')
def login_ok():
	user_list=[]
	user_list=user_select()
	return render_template('ok.html',user_list=user_list)

@app.route('/zhuce/',methods = ['GET','POST'])
def zhuce():
	username = request.form['username']
	password = request.form['password']
	age = request.form['age']
	address = request.form['address']
	user_insert(username,password,age,address)
	return '注册成功，恭喜成为VIP！！！'

if __name__=='__main__':
	app.run(port=8000, debug=True)