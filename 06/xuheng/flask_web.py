#coding=utf-8
__author__ = 'XuHeng'
from flask import Flask
from flask import render_template
from flask import Response
from flask import request,redirect
from opfile import write_file,read_file,check_key,check_phone_num
import sys


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/userinfo')
def userinfo():
    user_dict=read_file()
    return render_template('index.html',user_dict=user_dict)


@app.route('/login/', methods = ['POST'])
def GetLogin():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        user_dict=read_file()
        if username in user_dict.keys():
            if password == user_dict[username][0]:
                    return  redirect('/userinfo')
            else:
                    return  Response('密码错误')
        else:
            return  Response('帐号不存在')
    else:
         return Response('非法提交')

@app.route('/registe/', methods = ['POST'])
def GetRegiste():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        telephone=request.form.get('telephone')
        phone_result=check_phone_num(telephone)
        if phone_result != 'True':
            return  Response(phone_result)
        if check_key(username):
            return Response('帐号已存在!!请更换帐号，重试')
        if write_file(username,password,telephone):
            return Response('注册成功!!!')
    else:
         return Response('非法提交')


if __name__ == '__main__':
    app.run('0.0.0.0',18080,debug=True)

'''
不错，对用户输入进行了比较检查, 继续加油
需要注意几个问题
1. 文件内容编码声明必须放在代码之前 __author__=''也是python代码
2. 注意缩进格式化保持一致
3.  注意函数返回值类型尽量保持一致性, opfile.py line42, 在line53行 True != 'True' 为真, flask返回函数返回值必须是Response对象(Response中的参数也必须为字符串)或者字符串 
'''