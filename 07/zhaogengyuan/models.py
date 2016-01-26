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
def validate_user_add(username,password,age,address):
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
            port=gconf.DB_PORT, \
            user=gconf.DB_USER, \
            passwd=gconf.DB_PASSWD, \
            db=gconf.DB_DATABASE, \
            charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    count = cur.execute('INSERT INTO user(username,password,age,address) VALUES(%s,md5(%s),%s,%s)', \
                        (username,password,age,address))
    cur.close()
    conn.commit()
    conn.close()
    return count !=0

def query_user(username):
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
            port=gconf.DB_PORT, \
            user=gconf.DB_USER, \
            passwd=gconf.DB_PASSWD, \
            db=gconf.DB_DATABASE, \
            charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    count = cur.execute('SELECT * FROM user where username=%s')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if rows is not None:
        for row in rows:
            tmpstr = row[0]
            print "%s" % (tmpstr)
            if tmpstr == username:
                return True
            else:
                return False
    else:
        return True
