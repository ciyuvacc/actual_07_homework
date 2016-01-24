#encoding: utf-8
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
        return redirect('/')
@app.route('/users/')
def users():
    return 'Login Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
