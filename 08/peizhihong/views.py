# coding:utf-8

import os
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
import models

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods=['GET'])
@app.route('/index/', methods=['GET'])
def login():
	return render_template('login.html')

@app.route('/login/', methods=['GET', 'POST'])
def loginvalidate():
	if request.method == 'GET':
		name = request.args.get('username')
		password = request.args.get('password')
		return render_template('login.html', username=name)
	else:
		name = request.form.get('username')
		password = request.form.get('password')
		try:
			cmd_valid = "SELECT * FROM member WHERE username = %s AND password = md5(%s)"
			valid_res = models.db_select(cmd_valid, name, password)
			if valid_res:
				session['username'] = name
				return redirect(url_for('listUser'))
			else:
				return render_template('login.html', error=u'账号或密码错误', username=name)
		except Exception,e:
			return render_template('login.html', error=str(e))

@app.route('/logoff/', methods=['GET'])
def logoff():
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/createUser/')
def createUser():
	if session.get('username'):
		return render_template('create.html')
	else:
		return redirect(url_for('login'))

@app.route('/addUser/', methods=['POST'])
def addUser():
	if session.get('username'):
		name = request.form.get('username')
		password = request.form.get('password')
		password2 = request.form.get('password2')
		mobile = request.form.get('mobile')
		email = request.form.get('email')
		age = request.form.get('age')
		# 账号密码不为空
		if not name or not password:
			return render_template('create.html', error=u'账号或密码不能为空')
		# 密码要一致
		if password != password2:
			return render_template('create.html', error=u'两次密码输入不一致')
		# 账号存在判断
		cmd_name = "SELECT * FROM member WHERE username = %s"
		if models.db_select(cmd_name,name):
			return render_template('create.html', error=u'账号已存在')
		# 年龄判断
		if not age.isdigit():
			return render_template('create.html', error=u'年龄必须为整数')
		# 插入数据
		try:
			cmd_insert = "INSERT INTO member (username,password,mobile,email,age) VALUES (%s, md5(%s), %s, %s, %s)"
			models.db_execute(cmd_insert,name, password, mobile, email, int(age))
			return redirect('/listUser/')
		except Exception,e:
			return render_template('login.html', error=str(e))
	else:
		return redirect(url_for('login'))

@app.route('/listUser/', methods=['GET', 'POST'])
def listUser():
	if not session.get('username'):
		return redirect(url_for('login'))

	if request.method == 'POST':
		try:
			name = request.form.get('query')
			if name:
				cmd_list = "SELECT * FROM member WHERE username = %s"
				userLst = models.db_select(cmd_list,name)
				return render_template('list.html', users=userLst)
			else:
				cmd_list = "SELECT * FROM member"
				userLst = models.db_select(cmd_list)
				return render_template('list.html', users=userLst)
		except Exception,e:
			return render_template('login.html', error=str(e))
	else:
		return render_template('list.html')

@app.route('/modifyUser/')
def modifyUser():
	if not session.get('username'):
		return redirect(url_for('login'))
	name = request.args.get('username')
	cmd_list = "SELECT * FROM member WHERE username = %s"
	user = models.db_select(cmd_list, name)
	return render_template('update.html',username=name)

@app.route('/updateUser/', methods=['GET','POST'])
def updateUser():
	if not session.get('username'):
		return redirect(url_for('login'))
	if request.method == 'POST':
		name = request.form.get('username')
		password = request.form.get('password')
		mobile = request.form.get('mobile')
		email = request.form.get('email')
		age = request.form.get('age')
		if not password:
			return render_template('update.html', username=name, error=u'密码必须填写')
		# 年龄判断
		if not age.isdigit():
			return render_template('update.html', username=name, error=u'年龄必须为整数')
		try:
			cmd_insert = "UPDATE member SET password=md5(%s),mobile=%s,email=%s,age=%s WHERE username=%s"
			models.db_execute(cmd_insert, password,mobile,email,int(age),name)
			return render_template('list.html')
		except Exception,e: 
			return render_template('update.html', username=name, error=str(e))
	else:
		return render_template('list.html')

@app.route('/deleteUser/', methods=['GET'])
def deleteUser():
	if not session.get('username'):
		return redirect(url_for('login'))
	name = request.args.get('username')
	cmd_delete = "DELETE FROM member WHERE username = %s"
	try:
		models.db_execute(cmd_delete,name)
		return render_template('list.html')
	except Exception,e:
		return render_template('list.html',error=str(e))
