# coding:utf-8

# models.py

import MySQLdb

host = '127.0.0.1'
port = 3306
user = 'peizhihong'
passwd = '密码'
db = 'peizhihong'
charset = 'utf8'

def db_connect():
	conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
	return conn

def db_select(cmd,*args):
	conn = db_connect()
	cur = conn.cursor()
	cur.execute(cmd,args)
	result = cur.fetchall()
	cur.close()
	conn.close()
	return result

def db_execute(cmd,*args):
	conn = db_connect()
	cur = conn.cursor()
	cur.execute(cmd,args)
	conn.commit()
	cur.close()
	conn.close()

