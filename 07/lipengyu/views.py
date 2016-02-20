#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import models


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



#登录页面
@app.route('/login/',methods=["POST"]) 
def login():
    username = request.form.get('username','')
    password = request.form.get('password','')
    if models.validate_user_login(username,password):
    	return redirect('/main_page/')
    else:
    	return render_template('index.html', \
    		                  loginerror='用户名或密码错误', \
    		                  loginusername=username, \
    		                  loginpassword=password)

#注册
@app.route('/register/',methods=["POST"])
def register():
    username = request.form.get('username','')
    password = request.form.get('password','')
    age = request.form.get('age','')
    address = request.form.get('address','')
    ok,info = models.validate_user_add(username,password,age,address)
    if ok:
    	models.add_user(username,password,age,address)
    	info = '注册成功'

    return render_template('index.html',registerok=ok,registerinfo=info)


#修改数据
@app.route('/update/', methods=['GET','POST']) 
def genxin(): 
    if request.method == 'POST': 
        return render_template('update.html') 
@app.route('/updateone/',methods=['GET','POST']) 
def option(): 
    if request.method == 'POST': 
        username = request.form.get('user') 
        password = request.form.get('password') 
        age = request.form.get('age') 
        address = request.form.get('address') 
        if models.db_update(username,password, age, address): 
            return "数据被修改" 
        else: 
            return "数据修改失败" 


#注册成功
@app.route('/successful/') 
def successful(): 
    return "注册成功" 

#登录成功
@app.route('/login_successful/')
def login_successful():
    return "登陆成功"


#登录跳转
@app.route('/main_page/', methods=['GET','POST']) 
def main(): 
    if request.method == 'GET': 
        body = models.get_users() 
        return render_template('main_page.html', pages=body) 
    else: 
        return render_template('main_page.html') 




#全表扫描
@app.route('/users/')
def users():
    users = models.get_users()
    print users #打印出来的应该是列表或者元组
    return render_template('users.html',users=users)








if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8888,debug=True)
