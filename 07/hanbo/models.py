#coding:utf8
import MySQLdb
import db

#数据库连接函数
def dbconn():
    conn = MySQLdb.connect(host=db.DB_HOST,\
                         port=db.DB_PORT,\
                         user=db.DB_USER,\
                         passwd=db.DB_PASS,\
                         db=db.DB_DATABASE,\
                         charset=db.DB_CHARSET)
    cur = conn.cursor()
    conn.autocommit(1)
    return cur

#用户登录的时候验证用户名和密码
def validate_user_login(username,password):
    cur = dbconn()
    count = cur.execute('select * from user where username=%s and password=md5(%s)',(username,password))
    cur.close()
    return count != 0


                                                                                                                                


#用户注册
def user_register(username,password,age,address):
    cur = dbconn()
    count = cur.execute('insert into user(username,password,age,address) values(%s,md5(%s),%s,%s)',(username,password,age,address))
    cur.close()
    return True
#y验证用户注册    
def valid_user_register(username,password,age,address):

    return True,''   

#获取用户的信息：姓名，年龄，地址
def get_users():
    cur = dbconn()
    count = cur.execute('select username,age,address from user')
    users = cur.fetchall()
    cur.close()
    return users   


#验证用户名是否重复
def valid_user_name(username):
    cur = dbconn()
    result = cur.execute('select username from user where username=%s', username)
    cur.close()
    return result != 0

#判断年龄是否是数字
def isNum(age):
    try:
        age + 1
    except TypeError:
        return False
    else:
        return True


#编辑用户信息

def update_user(name,password,age,address):
    cur = dbconn()
    up = cur.execute('update user set name=%s,password=md5(%s),age=%s,address=%s', (username,password,age,address))
    cur.close()
    return up != 0

#删除用户信息
def delete_user(username):
    cur = dbconn()
    delete = cur.execute('delete from user where username=%s',username)
    cur.close()
    return delete != 0
