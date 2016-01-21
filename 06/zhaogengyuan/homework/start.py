#encoding: utf-8

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello reboot'

@app.route('/printname/')
def print_args():
    return 'hello, %s' % request.args.get('name')


@app.route('/login2/')
def login2():
    h = open('./html/login.html')
    cxt = h.read()
    h.close()
    return cxt.format(username=request.args.get('username'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)

@app.route('/login3/')
def login3():
    name = request.args.get('name')
    return render_template("login2.html", name=name, password='password')

@app.route('/validate/', methods=["post","get"])
def loginvalidate():
    if request.method == 'GET':
        name = request.args.get('username')
        password = request.args.get('password')
	return render_template("login2.html", name=username, password='password')
    else:
        name = request.form.get('username')
        password = request.form.get('password')
        if name == 'a' and password == 'password':
            return 'success: %s , %s , %s' % (name, password, request.method)
        else:
            return 'fail: %s , %s, %s' % (name,passworda,request.method)


