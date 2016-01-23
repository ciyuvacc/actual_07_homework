#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 引入flask中的必要类和函数
from flask import Flask              #创建Flask APP对象
from flask import request            #用于获取用户提交的数据
from flask import render_template    #加载模板
from flask import redirect           #重定向到其他url

# 导入自定义的模块
import user

# 创建一个Flask app
# Flask需要根据传递的参数去寻找templates, static等目录的位置
app = Flask(__name__)


# homepage
# 定义路由, 如果以GET方式访问url地址为/则由index函数处理
@app.route('/')
def index():
    # 返回templates目录下的login.html模板中的内容
    return render_template('login.html')

# 登陆验证
# 定义路由, 若以GET、POST方式提交请求到url地址/login/则有login函数处理
@app.route('/login/', methods=['GET', 'POST'])
def login():
    # 如果为GET请求则从request.args中获取提交的数据
    # 如果为POST请求则从request.form中获取提交的数据
    params = request.args if request.method == 'GET' else request.form
    
    # 获取username和password信息
    username = params.get('username', '')
    password = params.get('password', '')
    
    # 验证用户名和密码
    if user.validate_user_login(username, password):
        # 成功则显示所有用户的信息列表
        return redirect('/users/')
    else:
        # 失败则提示用户失败, 依然返回登陆页面
        return render_template('login.html', error='用户名或密码错误', login_username=username)


# 注册
# 定义路由, 若以POST方式提交请求到url地址/register/则有register函数处理
@app.route('/register/', methods=['POST'])
def register():
    # 从request.form中获取username、password、telephone信息
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    telephone = request.form.get('telephone', '')

    # 检查用户提交的数据
    ok, result = user.validate_user_add(username, password, telephone)
    
    # 如果检查通过则添加到文件中
    if ok:
        if user.add_user(username, password, telephone):
            ok = True
            result = '注册成功'
        else:
            ok = False
            result = '注册失败'

    return render_template('login.html', ok=ok, result=result, register_username=username, password=password, telephone=telephone)

# 获取用户列表
# 定义路由, 如果以GET方式访问url地址为/users/则由users函数处理
@app.route('/users/', methods=['GET'])
def users():
    # 获取所有用户
    _users = user.get_users()
    # 返回用户列表页面
    return render_template('users.html', users=_users.values())


# 以python app.py方式运行式__name__ == '__main__'为真, 此时执行if中的子语句
if __name__ == '__main__':
    # 启动app, 监听IP和端口为0.0.0.0:8888, 打开debug模式
    app.run(host='0.0.0.0', port=8888, debug=True)