from . import app
import json
from flask import url_for,request,render_template,redirect,make_response,session

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
    user = request.form['username']
    pwd = request.form['password']
    sql = 'select username,password from user where username = "%s" and password = md5("%s")'%(user,pwd)
    print sql
    tmp = app.config['cursor']._execute(sql)
    cur=tmp['cur'].fetchall()
    if cur != ():
        message='login success'
        session['username']=user
        return redirect('/index')
    else:
        return render_template('login.html',message='Bad username or password')
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('main'))

