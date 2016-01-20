# coding:utf-8

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import sqlite3
import mycalc

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return 'hello python'

@app.route('/printname/')
def print_args():
	return 'hello, %s' % request.args.get('name')

@app.route('/login/')
def login():
	return render_template('login.html')

@app.route('/validate/', methods=['post', 'get'])
def loginvalidate():
	if request.method == 'GET':
		name = request.args.get('username')
		password = request.args.get('password')
	else:
		name = request.form.get('username')
		password = request.form.get('password')
		try:
			conn =sqlite3.connect('Reboot.sqlite')
			cursor = conn.cursor()
			cmd1 = "SELECT * FROM user WHERE username == '%s' AND password == '%s'" % (name,password)
			cursor.execute(cmd1)
			if cursor.fetchall():
				return redirect('/users/')
			else:
				return render_template('login.html', info=u'账号或密码错误')
			cursor.close()
			conn.close()
		except Exception,e:
			return render_template('login.html', info=str(e))


@app.route('/record/', methods=['post'])
def record():
	name = request.form.get('username')
	password = request.form.get('password')
	password2 = request.form.get('password2')
	mobile = request.form.get('mobile')
	email = request.form.get('email')
	age = int(request.form.get('age'))
	if not password or (password != password2):
		return render_template('login.html', info=u'注册信息不正确')
	else:
		try:
			conn = sqlite3.connect('Reboot.sqlite')
			cursor = conn.cursor()
			cmd = "INSERT INTO user (username,password,mobile,email,age) values ('%s','%s','%s','%s',%d)" % (name,password,mobile,email,age)
			cursor.execute(cmd)
			conn.commit()
			cursor.close()
			conn.close()
			return render_template('login.html', info=u'注册成功')
		except Exception,e:
			return render_template('login.html', info=str(e))

@app.route('/users/')
def display_user():
	try:
		conn = sqlite3.connect('Reboot.sqlite')
		cursor = conn.cursor()
		cmd = "SELECT * FROM user"
		cursor.execute(cmd)
		user_list = cursor.fetchall()
		cursor.close()
		conn.close()
		return render_template('users.html', users=user_list)
	except Exception,e:
		return render_template('login.html', info=str(e))

@app.route('/calc/', methods=['get','post'])
def calc():
	if request.method == 'GET':
		return render_template('calc.html')
	else:
		expr = request.form.get('expr')
		if expr:
			try:
				res = mycalc.arithmeticEval(expr)
				return render_template('calc.html', expr = expr, calc_res = res)
			except Exception,e:
				return render_template('calc.html', info = str(e))
		else:
			return render_template('calc.html')

if __name__ == '__main__':
	app.run(debug=True,port=9090)
