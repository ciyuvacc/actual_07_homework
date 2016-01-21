#encoding: utf-8
from flask import Flask,request,render_template,redirect
from base import *
import json

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login' ,methods=['POST'])
def sys_login():
    pass_dict=sys_pass()
    user = request.form['username']
    pwd =request.form['password']
    if user in pass_dict and pass_dict[user]['password'] == pwd:
        return redirect('/log')
    else:
        return render_template('login.html',message='Bad username or password',loginuser=user)


@app.route('/sign',methods=['POST','GET'])
def sign():
    if request.method == 'POST':
        username =request.form.get('username')
        password =request.form.get('password')
        email =request.form.get('email')
        sex =request.form.get('inlineRadioOptions')
        age =request.form.get('age')
        pass_dict=sys_pass()
        print pass_dict
        if username =='' or password == '':
            return render_template('sign.html',message="username or password is null")
        elif username in pass_dict and username != None:
            return render_template('sign.html',message="%s already sign"%username)
        else:
            pass_dict[username]={'password':password,'email':email,'sex':sex,'age':age}
            sys_writepass(pass_dict)
            return render_template('sign.html',message='sign success',username=username,password=password)
    return render_template('sign.html')

@app.route('/log')
def log():
    return render_template('showlog.html')

@app.route('/showlog')
def showlog():
    infile='www_access_20140823.log'
    node = int(request.args.get('count')) 
    node += 1
    print 'node %s' % node
    arr_list=[]
    len_list = 0
    
    arr_list,len_list = count_log(infile,int(node))
    data_dict ={}
    data_dict['len']=len_list
    data_dict['data']=arr_list
    return json.dumps(data_dict)

@app.route('/operate')
def operate():
    mystr = request.args.get('mycount')
    mystr= mystr.encode("utf-8")
    count = init_func1(mystr)
    return str(count)
@app.route('/showpass')
def showpass():
    pass_dict=sys_pass()
    return json.dumps(pass_dict)

@app.route('/passchange')
def passchange():
    change= request.args.get('change')
    if change == 'delete':
        username =request.args.get('name')
        pass_dict=sys_pass()
        pass_dict.pop(username)
        sys_writepass(pass_dict)
        return 'ok'
    elif change == 'update':
        username =request.args.get('name')
        password =request.args.get('pass')
        email =request.args.get('email')
        sex =request.args.get('sex')
        age =request.args.get('age')
        pass_dict=sys_pass()
        pass_dict[username]={'password':password,'email':email,'sex':sex,'age':age}
        sys_writepass(pass_dict)
        return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090,debug=True)
