from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

import user

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == "GET":
		params = request.form
	else:
		params = request.args

	username = params.get('username', '')
	password = params.get('password', '')

	if user.val_user_login(username, password):
		return redirect('/users/')
	else:
		return render_template('login.html', error='username is incorrect or password is incorrect', login_username=username)

@app.route('/register/', methods=['POST'])
def register():
	username = request.form.get('username', '')
	password = request.form.get('password', '')
	telephone = request.form.get('telephone', '')

	status, result = user.val_user_add(username, password, telephone) 
	
	if status:
		if user.add_user(username, password, telephone):
			status = True
			result = "Success"
		else:
			status = False
			result = 'Failed'
	return render_template('login.html', status=status, result=result, register_username=username, password=password, telephone=telephone)

@app.route('/users/', methods=['GET'])
def users():
    _users = user.get_user()
    return render_template('users.html', users=_users.values())

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 8000, debug = True)
