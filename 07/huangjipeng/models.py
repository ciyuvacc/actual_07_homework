#encoding:utf8

import MySQLdb
import gconf

def mysql_conn():
    conn = MySQLdb.connect(host=gconf.DB_HOST,\
                        port=gconf.DB_PORT, \
                        user=gconf.DB_USER, \
                        passwd=gconf.DB_PASSWD, \
                        db=gconf.DB_DATABASE, \
                        charset=gconf.DB_CHARSET)
    return conn

def validate_user_login(username,password):
    
    cur = mysql_conn().cursor()
    count = cur.execute('select * from user where username=%s and password=md5(%s)', \
			(username,password))
    cur.close()
    mysql_conn().close()
    return count != 0

def validate_user_register(username,password,age,address):
    ok = True
    if username == '' or password == '':
        ok = False
	info = '用户名或密码不能为空'
    try:
        if ok is True:
            age = int(age)
    except BaseException as e:
            with open('user_error.log','a') as user_error:
                print >> user_error,e
		ok = False
                info = '年龄一栏应填写数字'
    if ok is True:
        conn = mysql_conn()
        cur = conn.cursor()
        count = cur.execute('select * from user where username=%s',(username,))
        cur.close()
        conn.close()
        if count == 0 and password.count('') > 6 and password.count('') <  32:
            ok = True
            info = ''
        elif count != 0 or count != 0 and password.count('') > 6 and password.count('') <  32:
            ok = False
	    info = '此用户已被占用'
        elif count == 0 and password.count('') < 6:
            ok = False
            info = '密码个数应该大于6个 '
        elif count == 0 and password.count('') > 32:
            ok = False
	    info = '密码个数不超于32个'
	else:
            ok = False
	    info = '未知错误'
    return ok,info


def add_user(username, password, age, address):
    conn = mysql_conn()
    cur = conn.cursor()
    
    count = cur.execute('INSERT INTO user(username, password, age, address) VALUES(%s, md5(%s), %s, %s) ', \
                        (username, password, age, address))
    conn.commit()
    cur.close()
    conn.close()
    return True

   
def get_users():
    conn = mysql_conn()
    cur = conn.cursor()
    count = cur.execute('SELECT * FROM user')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

def del_user(username):
    conn = mysql_conn()
    cur = conn.cursor()

    count = cur.execute("delete  from  user where username=%s",(username,))
    conn.commit()
    cur.close()
    conn.close()
    return count != 0
def mode_user(username,age,address):
    conn = mysql_conn()
    cur = conn.cursor()
    count = cur.execute("update user set age=%s,address=%s where username=%s",(age,address,username))
    conn.commit()
    cur.close()
    conn.close()
    return count != 0

def mode_setpassword(setusername,setpassword):
    if setpassword.count('') > 6 and setpassword.count('') < 32:
        conn = mysql_conn()
        cur = conn.cursor()
        count = cur.execute("update user set password=md5(%s) where username=%s",(setpassword,setusername))
        conn.commit()
        cur.close()
        conn.close()
        return True
    else:
        return False
def get_logs(n=10):
    conn = mysql_conn()
    cur = conn.cursor()
    count = cur.execute("select * from logs order by count desc limit 0,%s",(n,)) 
    logs = cur.fetchall()
    cur.close()
    conn.close()
    return logs

if __name__ == "__main__":
    print get_users()[1][2]
