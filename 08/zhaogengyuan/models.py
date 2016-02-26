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

def check_sql(sql):
    sql = sql
    conn = get_conn()
    cur = get_cur(conn)
    result = cur.execute(sql)
    conn.commit()
    close(cur,conn)
    return result

def query_sql(sql):
    sql = sql
    conn = get_conn()
    cur = get_cur(conn)
#    result = cur.fetchall()
    result = cur.execute(sql)
    close(cur,conn)
    return result

def query(sql):
    sql = sql
    conn = get_conn()
    cur = get_cur(conn)
    cur.execute(sql)
    result = cur.fetchall()
    close(cur,conn)
    return result

def validate_user_login(username,password):
    username = username
    password = password
    sql = 'SELECT * FROM user where username=\'%s\' and password=md5(\'%s\')' % (username,password)
    result = query_sql(sql)
    return result != 0

def validate_user_add(username,password,age,address):
    username = username
    password = password
    age = age
    address = address
    sql = 'INSERT INTO user(username,password,age,address) VALUES(\'%s\',md5(\'%s\'),\'%s\',\'%s\')' % (username,password,age,address)
    result = check_sql(sql)
    return result !=0

def query_user(username):
    username = username
    if username=='':
        sql = 'SELECT * FROM user'
    else:
        sql = 'SELECT username FROM user where username=\'%s\'' % (username,)
    result = query(sql)
    return result
