from . import app 
import json
from flask import request,render_template,redirect,make_response,session

@app.route('/upuser')
def adduser():
    return render_template('up.html',username=session['username'])

@app.route('/changeuser',methods=['POST'])
def changeuser():
    change = request.form.get('change')
    username =request.form.get('username')
    if "show" == change:
        sql = 'select *  from user where username = "%s"'%(username)
        tmp = app.config['cursor']._execute(sql)
        cur=tmp['cur'].fetchall()
        return json.dumps(cur)
    elif "update" == change:
        password =request.form.get('password')
        email =request.form.get('email')
        age =request.form.get('age')
        sex =request.form.get('sex')
        address =request.form.get('address')
        sql = 'update user set password=md5("%s"),email="%s",age="%s",sex="%s",address="%s" where username="%s" '%(password,email,age,sex,address,username)
        print sql
        tmp = app.config['cursor']._execute(sql)
        cur=tmp['msg']
        return cur
