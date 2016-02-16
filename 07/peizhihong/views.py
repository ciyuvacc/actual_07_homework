# coding:utf-8

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import models

app = Flask(__name__)

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
				return redirect('/listUser/')
			else:
				return render_template('login.html', info=u'账号或密码错误', username=name)
		except Exception,e:
			return render_template('login.html', info=str(e))

@app.route('/createUser/')
def createUser():
	return render_template('create.html')

@app.route('/addUser/', methods=['POST'])
def addUser():
	name = request.form.get('username')
	password = request.form.get('password')
	password2 = request.form.get('password2')
	mobile = request.form.get('mobile')
	email = request.form.get('email')
	age = request.form.get('age')
	# 账号密码不为空
	if not name or not password:
		return render_template('login.html', info=u'账号或密码不能为空')
	# 密码要一致
	if password != password2:
		return render_template('login.html', info=u'两次密码输入不一致')
	# 账号存在判断
	cmd_name = "SELECT * FROM member WHERE username = %s"
	if models.db_select(cmd_name,name):
		return render_template('login.html', info=u'账号已存在')
	# 年龄判断
	if not age.isdigit():
		return render_template('login.html', info=u'年龄必须为整数')
	# 插入数据
	try:
		cmd_insert = "INSERT INTO member (username,password,mobile,email,age) VALUES (%s, md5(%s), %s, %s, %s)"
		models.db_execute(cmd_insert,name, password, mobile, email, int(age))
		return redirect('/listUser/')
	except Exception,e:
		print str(e)
		return render_template('login.html', info=str(e))

@app.route('/listUser/', methods=['GET', 'POST'])
def listUser():
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
			return render_template('login.html', info=str(e))
	else:
		return render_template('list.html')

@app.route('/modifyUser/')
def modifyUser():
	name = request.args.get('username')
	cmd_list = "SELECT * FROM member WHERE username = %s"
	user = models.db_select(cmd_list, name)
	return render_template('update.html',user=user)

@app.route('/updateUser/', methods=['GET','POST'])
def updateUser():
	if request.method == 'POST':
		name = request.form.get('username')
		password = request.form.get('password')
		mobile = request.form.get('mobile')
		email = request.form.get('email')
		age = request.form.get('age')
		# 年龄判断
		if not age.isdigit():
			return render_template('update.html', info=u'年龄必须为整数')
		try:
			cmd_insert = "UPDATE member SET password=md5(%s),mobile=%s,email=%s,age=%s WHERE username=%s"
			models.db_execute(cmd_insert, password,mobile,email,int(age),name)
			return render_template('list.html')
		except Exception,e: 
			return render_template('update.html', info=str(e))
	else:
		return render_template('list.html')

@app.route('/deleteUser/', methods=['GET'])
def deleteUser():
	name = request.args.get('username')
	cmd_delete = "DELETE FROM member WHERE username = %s"
	try:
		models.db_execute(cmd_delete,name)
		return render_template('list.html')
	except Exception,e:
		return render_template('list.html',info=str(e))

if __name__ == '__main__':
	app.run(debug=True,port=9090)
