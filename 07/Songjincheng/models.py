#!/usr/bin/env python
#-*- coding:utf-8 -*-


import MySQLdb as mysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import gconf


def mysql_add(username, password, age, email, IPhone):
    conn = mysql.connect(host=gconf.DB_HOST, \
                   port=gconf.DB_PORT, \
                   user=gconf.DB_USER, \
                   passwd=gconf.DB_PASS, \
                   db=gconf.DB_DATABASE, \
                   charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    count = cur.execute('insert into user (username, password, age, email, IPhone) values(%s, %s, %s, %s, %s)', \
    (username, password, age, email, IPhone))
    cur.close()
    conn.close()
    return count != 0


def mysql_del(id):
    conn = mysql.connect(host=gconf.DB_HOST, \
                       port=gconf.DB_PORT, \
                       user=gconf.DB_USER, \
                       passwd=gconf.DB_PASS, \
                         db=gconf.DB_DATABASE, \
                       charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    SQL = 'delete from user where id=%d' % int(id)
    count = cur.execute(SQL)
    cur.close()
    conn.close()
    return count != 0

def mysql_delbackup(username, password, age, email, IPhone):
    conn = mysql.connect(host=gconf.DB_HOST, \
                   port=gconf.DB_PORT, \
                   user=gconf.DB_USER, \
                   passwd=gconf.DB_PASS, \
                   db=gconf.DB_DATABASE, \
                   charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    count = cur.execute('delete from user where username=%s, and password=%s, age=%s, email=%s and IPhone=%s', \
    (username, password, age, email, IPhone))
    cur.close()
    conn.close()
    return count != 0


def mysql_update(password, age, email, IPhone, username):
    conn = mysql.connect(host=gconf.DB_HOST, \
                    port=gconf.DB_PORT, \
                    user=gconf.DB_USER, \
                    passwd=gconf.DB_PASS, \
                    db=gconf.DB_DATABASE, \
                    charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    count = cur.execute('update user set password=%s, age=%s, email=%s, IPhone=%s where username=%s', \
    (password, age, email, IPhone, username))
    return count != 0

#select * from user where username='xiaosong';

def mysql_update1(username):
    conn = mysql.connect(host=gconf.DB_HOST, \
                          port=gconf.DB_PORT, \
                          user=gconf.DB_USER, \
                          passwd=gconf.DB_PASS, \
                          db=gconf.DB_DATABASE, \
                          charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    SQL = 'SELECT * FROM user where username=%s' % username
    count = cur.execute(SQL)
    data = count.fetchall()    
    return data
    cur.close()
    conn.close()

#update user set password='123.com', age=26, email='567@.com', IPhone='7890' where username="xiaoliu";


def mysql_select(username):
    conn = mysql.connect(host=gconf.DB_HOST, \
                port=gconf.DB_PORT, \
                user=gconf.DB_USER, \
                passwd=gconf.DB_PASS, \
                db=gconf.DB_DATABASE, \
                charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    SQL = "select * from user where username='%s';" % username
    cur.execute(SQL)
    data = cur.fetchall()
    return data
    cur.close()
    conn.close()

#SELECT * FROM user where username='xiaoliu';

def mysql_cat():
    user_dic = {}
    conn = mysql.connect(host=gconf.DB_HOST, \
              port=gconf.DB_PORT, \
              user=gconf.DB_USER, \
              passwd=gconf.DB_PASS, \
              db=gconf.DB_DATABASE, \
              charset=gconf.DB_CHARSET)
    cur = conn.cursor()
    sql_select = "select * from user;"
    cur.execute(sql_select)
    data = cur.fetchall()
    return data
    cur.close()
    conn.close()









