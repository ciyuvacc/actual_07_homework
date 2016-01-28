#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import logstat

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login/', methods = ['GET','POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	if username=='2' and password=='2':
		return redirect('logs')
	else:
		return render_template('index.html', message='Bad username or password')

@app.route('/logs/')
def logs():
	stat_dict=logstat.read_log_file('access.log')
	result_list = logstat.get_top_10(stat_dict)
	return render_template('logs.html',logs=result_list)

if __name__=='__main__':
	app.run(port=8000, debug=True)