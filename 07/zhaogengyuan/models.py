#encoding: utf-8
import MySQLdb
import gconf

def validate_user_login(username,password):
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
            port=gconf.DB_PORT, \
            user=gconf.DB_USER, \
            passwd=gconf.DB_PASSWD, \
            db=gconf.DB_DATABASE, \
            charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    count = cur.execute('SELECT * FROM user where username=%s and password=md5(%s)', \
            (username,password))
    cur.close()
    conn.close()
    return count != 0
def user_register(username,password):
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
            port=gconf.DB_PORT, \
            user=gconf.DB_USER, \
            passwd=gconf.DB_PASSWD, \
            db=gconf.DB_DATABASE, \
            charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    count = cur.execute('SELECT * FROM user where username=%s and password=md5(%s)', \
            (username,password))
    cur.close()
    conn.close()




    return count != 0
