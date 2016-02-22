#coding=utf-8
import MySQLdb
import dbconf
from logshow import *

def connect_mysql():
    return MySQLdb.connect(host=dbconf.DBHOST,port=dbconf.DBPORT,user=dbconf.DBUSER,db=dbconf.DBNAME,charset=dbconf.DBCHARSET)

def add_user(username,password,email):
    conn = connect_mysql()
    cur = conn.cursor()
    count = cur.execute("insert into accout (username,password,email,createtime) values(%s,md5(%s),%s,now())",(username,password,email))
    conn.commit()
    cur.close()
    conn.close()
    return True

def exist_user(username,email=""):
    conn = connect_mysql()
    cur = conn.cursor()
    count = cur.execute("select * from accout where username=%s or email=%s",(username,email))
    cur.close()
    conn.close()
    return count == 0

def auth_user(username,password):
    conn = connect_mysql()
    cur = conn.cursor()
    count = cur.execute("select * from accout where username=%s and password=md5(%s)",(username,password))
    cur.close()
    conn.close()
    return count != 0

def get_user(selectuser=""):
    dict_user=['id','username','password','email','create_time']
    conn = connect_mysql()
    cur = conn.cursor()
    if selectuser == "":
        count = cur.execute("select * from accout")
        users = cur.fetchall()
    else:
        count = cur.execute("select * from accout where username=%s;",(selectuser,))
        users = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(zip(dict_user,user)) for user in users]

def modify_user(password,email,id):
    conn = connect_mysql()
    cur = conn.cursor()
    count = cur.execute("update accout set password=md5(%s),email=%s where id=%s",(password,email,int(id)))
    conn.commit()
    cur.close()
    conn.close()
    return True

def delete_user(username):
    conn = connect_mysql()
    cur = conn.cursor()
    count = cur.execute("delete from accout where username=%s",(username,))
    conn.commit()
    cur.close()
    conn.close()
    return True


def get_log():
    conn = connect_mysql()
    cur = conn.cursor()
    for s in _list:
        sql = 'insert  nginx_log values(%s,%s,%s,%s)' % s
        count = cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def show_log(numbers=10):
    conn = connect_mysql()
    cur = conn.cursor()
    count = cur.execute('select * from nginx_log order by count desc limit %s ;',int(numbers))
    logs = cur.fetchall()
    cur.close()
    conn.close()
    return logs






