#encoding: utf-8
import MySQLdb
import gconf

def get_conn():
    conn = MySQLdb.connect(host=gconf.DB_HOST, \
            port=gconf.DB_PORT, \
            user=gconf.DB_USER, \
            passwd=gconf.DB_PASSWD, \
            db=gconf.DB_DATABASE, \
            charset=gconf.DB_CHARSET)
    return conn

def get_cur(conn):
    cur = conn.cursor()
    return cur

def conn_close(conn):
    if conn != None:
        conn.close()

def cur_close(cur):
    if cur != None:
        cur.close()

def close(cur,conn):
    cur_close(cur)
    conn_close(conn)

def validate_user_login(username,password):
    conn = get_conn()
    cur = get_cur(conn)
    count = cur.execute('SELECT * FROM user where username=%s and password=md5(%s)', \
            (username,password))
    close(cur,conn)
    return count != 0

def validate_user_add(username,password,age,address):
    conn = get_conn()
    cur = get_cur(conn)
    count = cur.execute('INSERT INTO user(username,password,age,address) VALUES(%s,md5(%s),%s,%s)', \
                        (username,password,age,address))
    conn.commit()
    close(cur,conn)
    return count !=0

def query_user(username):
    conn = get_conn()
    cur = get_cur(conn)
    count = cur.execute('SELECT username FROM user where username=%s', (username,))
    rows = cur.fetchall()
    close(cur,conn)
    if rows is not None:
        for row in rows:
            tmpstr = row[0]
            if tmpstr == username:
                return True
            else:
                return False
    else:
        return True
