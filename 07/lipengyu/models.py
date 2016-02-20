#encoding:utf-8
import MySQLdb
import gconf
#用来验证用户名和密码是否正确如果正确返回返回True 如果失败返回false
def validate_user_login(username,password):
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
		            port=gconf.DB_PORT, \
		            user=gconf.DB_USER, \
		            passwd=gconf.DB_PASSWD, \
		            db=gconf.DB_DATABASE, \
		            charset=gconf.DB_CHARSET)
    cur = conn.cursor() 
    count = cur.execute('select * from user where username=%s and password=md5(%s)', \
    	               (username,password))
    print "调试模式,注册账号是%s 注册密码是%s 是否注册成功%s" %(username,password,count)
    cur.close()
    conn.close()
    return count != 0

def validate_user_add(username,password,age,address):
    return True, ''

#insert into 
def add_user(username,password,age,address):
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
		            port=gconf.DB_PORT, \
		            user=gconf.DB_USER, \
		            passwd=gconf.DB_PASSWD, \
		            db=gconf.DB_DATABASE, \
		            charset=gconf.DB_CHARSET)
    cur = conn.cursor() 
    count = cur.execute('INSERT INTO user(username,password,age,address) VALUES(%s,md5(%s),%s,%s)', \
    	               (username,password,age,address))
    conn.commit()
    cur.close()
    conn.close()
    return True

#update
def db_update(username,password,age,address):
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
                    port=gconf.DB_PORT, \
                    user=gconf.DB_USER, \
                    passwd=gconf.DB_PASSWD, \
                    db=gconf.DB_DATABASE, \
                    charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    count = cur.execute('update user set username=%s,password=%s,age=%s,address=%s', \
                        (username,password,age,address))
    return count !=0 





#select * from 
def get_users():
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
		            port=gconf.DB_PORT, \
		            user=gconf.DB_USER, \
		            passwd=gconf.DB_PASSWD, \
		            db=gconf.DB_DATABASE, \
		            charset=gconf.DB_CHARSET)
    cur = conn.cursor() 
    count = cur.execute('SELECT * FROM user')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users  
