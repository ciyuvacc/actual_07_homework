# coding:utf-8

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
from functools import wraps
import models
import json

app = Flask(__name__)
app.secret_key = r'\xcd\xf8\xca\xfc\xd3\xf0P\x92\x81\xc5?A}\x03\x8e*\x80\x80[v\xeb\xd9\xee(\x93@m\xc4\xed\xba\xef\x8f'

def login_required(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		if session.get('username') is None:
			return redirect(url_for('index'))
		else:
			return func(*args, **kwargs)
	return wrapper


@app.route('/', methods=['GET'])
def index():
	return render_template('login.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
	params = request.args if request.method == 'GET' else request.form

	name = params.get('username', '')
	password = params.get('password', '')

	if models.validate_user_login(name, password):
		session['username'] = name
		return redirect(url_for('listUser'))
	else:
		return render_template('login.html', error=u'用户名或密码错误', username=name)
	

@app.route('/register/', methods=['POST'])
def register():
	name = request.form.get('username', '')
	password = request.form.get('password', '')
	telephone = request.form.get('telephone', '')
	age = request.form.get('age', '')

	# models.validate_user_add返回(True,'')或者('False',原因)
	ok, result = models.validate_user_add(name, password, telephone, age)

	if ok:
		# models.add_user的返回值会与0比较，返回True或者False
		if models.add_user(name, password, telephone, age):
			ok = True
			result = u'注册成功'
		else:
			ok = False
			result = u'注册失败'

	return render_template('login.html', ok=ok, result=result, username=name, 
		password=password, telephone=telephone, age=age)


@app.route('/logoff/', methods=['GET'])
def logoff():
	session.clear()
	return redirect(url_for('index'))


@app.route('/createUser/')
@login_required
def createUser():
	return render_template('create.html')


@app.route('/addUser/', methods=['POST', 'GET'])
@login_required
def addUser():
	name = request.form.get('username', '')
	password = request.form.get('password', '')
	telephone = request.form.get('telephone', '')
	age = request.form.get('age', '')

	ok, result = models.validate_user_add(name, password, telephone, age)

	if ok:
		if models.add_user(name, password, telephone, age):
			ok = True
			result = u'注册成功'
		else:
			ok = False
			result = u'注册失败'
	if ok:
		return redirect(url_for('listUser'))
	else:
		return render_template('create.html', result=result, username=name, 
			password=password, telephone=telephone, age=age)


@app.route('/listUser/', methods=['GET', 'POST'])
@login_required
def listUser():
	params = request.args if request.method == 'GET' else request.form
	_query = params.get('query', '')
	_users = models.get_users(_query)
	return render_template('list.html', users=_users, query=_query)


@app.route('/modifyUser/')
@login_required
def modifyUser():
	_id = request.args.get('id', '')
	_user = models.get_user_by_id(_id)
	if _user is None:
		return render_template('update.html', result=u'用户信息不存在')
	else:
		return render_template('update.html', id=_user['id'], username=_user['username'], 
			telephone=_user['telephone'], age=_user['age'])


@app.route('/updateUser/', methods=['POST'])
@login_required
def updateUser():
	_id = request.form.get('id', '')
	_user = models.get_user_by_id(_id)
	if _user is None:
		return render_template('update.html', result=u'用户信息不存在')
	else:
		telephone = request.form.get('telephone', '')
		age = request.form.get('age', '')

		ok ,result = models.validate_user_modify(telephone, age)

		if ok:
			if models.modify_user(_user['id'], telephone, age):
				ok = True
				reuslt = u'更新成功'
			else:
				ok = False
				result = u'更新失败'
		if ok:
			return json.dumps({'ok': True})
		else:
			return json.dumps({'ok': False, 'result': result})


@app.route('/deleteUser/', methods=['GET'])
@login_required
def deleteUser():
	_id = request.args.get('id', '')
	models.delete_user(_id)
	return redirect(url_for('listUser'))

# 资产处理函数
@app.route('/asset/', methods=['GET', 'POST'])
@login_required
def asset():
	params = request.args if request.method == 'GET' else request.form
	_query = params.get('query', '')
	_assets = models.get_assets(_query)
	return render_template('asset.html',assets = _assets, query = _query)


@app.route('/machine_room/',methods=['GET'])
def machine_room():
	return json.dumps(models.get_machine_room())


@app.route('/addAsset/',methods=['POST'])
def addAsset():
	sn = request.form.get('sn', '')
	vendor = request.form.get('vendor', '')
	machine_room = request.form.get('machine_room', '')
	model = request.form.get('model', '')
	purchase_date = request.form.get('purchase_date', '')
	cpu = request.form.get('cpu', '')
	ram = request.form.get('ram', '')
	disk = request.form.get('disk', '')
	os = request.form.get('os', '')
	ip = request.form.get('ip', '')
	hostname = request.form.get('hostname', '')
	admin = request.form.get('admin', '')
	business = request.form.get('business', '')
	# 检查用户提交的数据
	ok, result = models.validate_asset_add(sn, vendor, machine_room, model, purchase_date, cpu, ram, disk, os, ip, hostname, admin, business)

	if ok:
		if models.add_asset(sn, vendor, machine_room, model, purchase_date, cpu, ram, disk, os, ip, hostname, admin, business):
			ok = True
			result = u'添加成功'
		else:
			ok = False
			result = u'添加失败'

	if ok:
		return render_template('asset.html')
	else:
		return render_template('asset.html', result=result, sn=sn, vendor=vendor, machine_room=machine_room, 
			model=model, purchase_date=purchase_date, cpu=cpu, ram=ram, disk=disk, os=os, ip=ip, hostname=hostname, 
			admin=admin, busines=business)

			
	return json.dumps({'ok': ok, 'result': result})


@app.route('/updateAsset/', methods=['POST'])
@login_required
def updateAsset():
	_id = request.form.get('id', '')
	_asset = models.get_asset_by_id(_id)
	if _asset is None:
		return render_template('asset.html', result=u'资产信息不存在')
	else:
		cpu = request.form.get('cpu', '')
		ram = request.form.get('ram','')
		disk = request.form.get('disk', '')

		ok ,result = models.validate_asset_modify(cpu, ram, age)

		if ok:
			if models.modify_asset(_asset['id'], cpu, ram, age):
				ok = True
				reuslt = u'更新成功'
			else:
				ok = False
				result = u'更新失败'
		if ok:
			return json.dumps({'ok': True})
		else:
			return json.dumps({'ok': False, 'result': result})

@app.route('/deleteAsset/', methods=['GET'])
@login_required
def deleteAsset():
	_id = request.args.get('id', '')
	models.delete_asset(_id)
	return redirect(url_for('asset'))