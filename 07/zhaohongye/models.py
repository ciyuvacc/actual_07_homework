#encoding: utf-8
import MySQLdb
import gconf
# 用来认证用户名和密码是否正确, 如果正确返回True, 如果错误返回False
def validate_user_login(username, password):
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
                    port=gconf.DB_PORT, \
                    user=gconf.DB_USER, \
                    passwd=gconf.DB_PASSWD, \
                    db=gconf.DB_DATABASE, \
                    charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    count = cur.execute('SELECT * FROM user where username=%s and password=md5(%s)', \
                        (username, password))
    cur.close()
    conn.close()
    return count != 0

def user_select():
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
                    port=gconf.DB_PORT, \
                    user=gconf.DB_USER, \
                    passwd=gconf.DB_PASSWD, \
                    db=gconf.DB_DATABASE, \
                    charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    cur.execute('SELECT * FROM user')
    user_list = list(cur.fetchall())
    cur.close()
    conn.close()
    return user_list

def user_insert(username,password,age,address):
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
                    port=gconf.DB_PORT, \
                    user=gconf.DB_USER, \
                    passwd=gconf.DB_PASSWD, \
                    db=gconf.DB_DATABASE, \
                    charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    cur.execute('insert into user(username,password,age,address) \
             values(%s,md5(%s),%s,%s)' % (username,password,age,address) )
    conn.commit()
    cur.close()
    conn.close()