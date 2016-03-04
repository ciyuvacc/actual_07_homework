# coding:utf-8

# dbutil.py

import gconf
import MySQLdb

def execute_sql(sql, args=(), is_fetch=False):
	_conn, _cur = None, None
	_rt_cnt, _rt_fetch = 0, ()

	try:
		_conn = MySQLdb.connect(host=gconf.host, 
			port=gconf.port, 
			user=gconf.user, 
			passwd=gconf.passwd, 
			db=gconf.db, 
			charset=gconf.charset)

		_cur = _conn.cursor()

		_rt_cnt = _cur.execute(sql,args)
		if is_fetch:
			_rt_fetch = _cur.fetchall()
		else:
			_conn.commit()
	except Exception, e:
		print str(e)
	finally:
		if _cur is not None:
			_cur.close()
		if _conn is not None:
			_conn.close()

	return _rt_cnt, _rt_fetch

if __name__ == '__main__':
	# 添加用户
	print execute_sql('INSERT INTO user(username,password) VALUES(%s,md5(%s));', ('zhaoyun','1234'))
	# 验证登录
	print execute_sql('SELECT * FROM user WHERE username=%s AND password=md5(%s);', ('zhaoyun','1234'), True)
	# 更改用户密码
	print execute_sql('UPDATE user SET password=md5(%s) WHERE username=%s;', ('123456','zhaoyun'))
	# 验证登录
	print execute_sql('SELECT * FROM user WHERE username=%s AND password=md5(%s);', ('zhaoyun','1234'), True)
	# 删除用户
	print execute_sql('DELETE FROM user WHERE username=%s;', ('zhaoyun',))

	# 添加5个用户
	for i in range(1,6):
		execute_sql('INSERT INTO user(username,password) VALUES(%s,md5(%s));',('user%s' % i, '123456'))

	# 查询所用用户
	_cnt, _rt = execute_sql('SELECT * FROM user', (), True)
	print _cnt
	for _rs in _rt:
		print _rs

	# 删除所有用户
	print execute_sql('DELETE FROM user')

	# 获取用户数量
	print execute_sql(sql='SELECT count(*) FROM user;', is_fetch=True)