#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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
        return redirect('/listUser/')
    else:
        return render_template('login.html', \
            login_error='用户名或密码错误')

@app.route('/createUser/')
def createUser():
    return render_template('create.html')




@app.route('/addUser/', methods=["POST"])
def addUser():
    username = request.form.get('username','')
    password = request.form.get('password','')
    age = request.form.get('age','')
    address = request.form.get('address','')
    if models.query_user(username):
        return render_template('index.html', \
                        register_error='注册失败，用户名重复', \
                        username=username)
    elif isNone(password):
        return render_template('index.html', \
                        register_error='注册失败，密码为空', \
                        password=password)
    elif isNotNum(age):
        return render_template('index.html', \
                        register_error='注册失败，年龄必须为数字', \
                        username=username, \
                        password=password, \
                        age=age, \
                        address=address)
    else:
        models.validate_user_add(username,password,age,address)
        return '新增成功'


 
@app.route('/register/', methods=["POST"])
def register():
    username = request.form.get('username','')
    password = request.form.get('password','')
    age = request.form.get('age','')
    address = request.form.get('address','')
    if models.query_user(username):
        return render_template('index.html', \
                        register_error='注册失败，用户名重复', \
                        username=username)
    elif isNone(password):
        return render_template('index.html', \
                        register_error='注册失败，密码为空', \
                        password=password)
    elif isNotNum(age):
        return render_template('index.html', \
                        register_error='注册失败，年龄必须为数字', \
                        username=username, \
                        password=password, \
                        age=age, \
                        address=address)
    else:
        models.validate_user_add(username,password,age,address)
        return '注册成功'

#@app.route('/listUser/')
@app.route('/listUser/',methods=['GET','POST'])
def listUser():
    username = request.form.get('query','')
    users=models.query_user(username)
    if users:
        return render_template('list.html', \
                    user=username, \
                    users=users)
    else:
        return 'none'

def isNone(string):
    if string:
        return False
    else:
        return True

def isNotNum(num):
    try:
        x = int(num)
    except TypeError:
        return True
    except ValueError:
        return True
    except Exception, e:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)

