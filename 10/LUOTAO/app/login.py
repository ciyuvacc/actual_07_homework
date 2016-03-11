#encoding: utf-8

from . import app
import json
from module import login_required,User
from flask import render_template,request,session,url_for,redirect

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        user = User(request.form)
        status =  user._login()
        if status:
            message='login success'
            session['username']=username
            return redirect('/index')
        else:
            return render_template('login.html',message='Bad username or password')
    else:
        return redirect('/')
    

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('main'))

