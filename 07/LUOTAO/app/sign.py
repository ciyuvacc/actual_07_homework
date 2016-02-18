from . import app
import json
from flask import request

@app.route('/sign',methods=['POST','GET'])
def sign():
    if request.method == 'POST':
        username =request.form.get('username')
        password =request.form.get('password')
        email =request.form.get('email')
        sex =request.form.get('sex')
        age =request.form.get('age')
        address =request.form.get('address')
        sql = 'select *  from user where username = "%s"'%(username)
        tmp = app.config['cursor']._execute(sql)
        cur=tmp['cur'].fetchall()
        print cur
        print 1111
        if cur != ():
            return 'user already exists'
        else:
            sql = 'insert into user (username,password,age,email,sex,address) values ("%s",md5("%s"),"%s","%s","%s","%s")'%(username,password,age,email,sex,address)
            print sql
            tmp = app.config['cursor']._execute(sql)
            cur=tmp['cur'].fetchall()
            print tmp
            return tmp['msg']
