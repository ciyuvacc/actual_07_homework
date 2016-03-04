# coding:utf-8

# models.py

from dbutil import execute_sql

# user表创建
'''
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(32) NOT NULL,
    `password` VARCHAR(32) NOT NULL,
    `telephone` VARCHAR(11) DEFAULT '',
    `age` INT DEFAULT 0,
    `sex` BOOLEAN DEFAULT 1,
    `status` INT DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

# user表中定义的用户属性
COLUMN_USER = ['id', 'username', 'password', 'telephone', 'age', 'sex', 'status']

# 查询所有用户信息的SQL语句
SQL_FETCH_ALL = 'SELECT %s FROM user;' % ', '.join(COLUMN_USER)

# 根据用户名查询用户信息的SQL语句
SQL_FETCH_BY_USERNAME = 'SELECT %s FROM user WHERE username like %%s;' % ', '.join(COLUMN_USER)

# 根据用户主键获取用户信息的SQL语句
SQL_GET_BY_ID = 'SELECT %s FROM user WHERE id = %%s LIMIT 1;' % ', '.join(COLUMN_USER)

# 根据用户名获取用户信息的SQL语句
SQL_GET_BY_USERNAME = 'SELECT %s FROM user WHERE username = %%s LIMIT 1;' % ', '.join(COLUMN_USER)

# 根据用户名密码查询用户信息数量的SQL语句
SQL_VALIDATE_LOGIN = 'SELECT * FROM user WHERE username = %s AND password = md5(%s) LIMIT 1;'

# 添加用户信息
SQL_INSERT = 'INSERT INTO user(username, password, telephone, age, sex, status) VALUES(%s, md5(%s), %s, %s, %s, %s);'

# 更新用户信息
SQL_MODIFY = 'UPDATE user SET telephone = %s, age = %s, sex = %s, status = %s WHERE id = %s';

# 根据用户主键ID删除用户
SQL_DELETE_BY_ID = 'DELETE FROM user WHERE id=%s;'

# asset表中定义的资产属性
COLUMN_ASSET = ['id', 'sn', 'vendor', 'machine_room_id', 'model', 'purchase_date', 'cpu', 'ram', 'disk', 
'os', 'ip', 'hostname', 'admin', 'business', 'status']

# 获取资产所在机房的信息
SQL_FETCH_MACHINE_ROOM = 'SELECT id, name FROM machine_room'

# 查询所有资产信息的SQL语句
SQL_FETCH_ASSET_ALL = 'SELECT %s FROM asset;' % ', '.join(COLUMN_ASSET)

# 根据SN查询资产信息的SQL语句
SQL_FETCH_ASSET_BY_SN = 'SELECT %s FROM asset WHERE sn like %%s;' % ', '.join(COLUMN_ASSET)

# 根据资产主键获取资产信息的SQL语句
SQL_GET_ASSET_BY_ID = 'SELECT %s FROM asset WHERE id = %%s LIMIT 1;' % ', '.join(COLUMN_ASSET)

# 根据SN获取资产信息的SQL语句
SQL_GET_ASSET_BY_SN = 'SELECT %s FROM asset WHERE sn = %%s LIMIT 1;' % ', '.join(COLUMN_ASSET)

# 添加资产信息
SQL_ASSET_INSERT = 'INSERT INTO asset(sn, vendor, machine_room_id, model, purchase_date, cpu, ram, disk, os, ip, hostname, \
admin, business) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'

# 更新资产信息
SQL_ASSET_MODIFY = 'UPDATE asset SET cpu = %s, ram = %s, disk = %s WHERE id = %s';

# 根据资产主键ID删除资产
SQL_DELETE_ASSET_BY_ID = 'DELETE FROM asset WHERE id=%s;'

# 获取所用用户的信息
def get_users(query=''):
	if query == '':
		_cnt, _users = execute_sql(SQL_FETCH_ALL, (), True)
	else:
		_cnt, _users = execute_sql(SQL_FETCH_BY_USERNAME,('%%%s%%' % query,), True)
	return [dict(zip(COLUMN_USER, _user)) for _user in _users]

# 根据用户主键获取用户的信息
def get_user_by_id(uid):
	_cnt, _users = execute_sql(SQL_GET_BY_ID, (uid,), True)
	return dict(zip(COLUMN_USER, _users[0])) if _cnt > 0 else None

# 根据用户名获取用户的信息
def get_user_by_username(username):
	_cnt, _users = execute_sql(SQL_GET_BY_USERNAME, (username,), True)
	return dict(zip(COLUMN_USER, _users[0])) if _cnt > 0 else None

# 验证用户登录时信息是否正确
def validate_user_login(username, password):
	_cnt, _ = execute_sql(SQL_VALIDATE_LOGIN, (username, password), True)
	# 与0比较返回True或者False
	return _cnt > 0

# 验证用户添加信息是否正确
def validate_user_add(username, password, telephone, age, sex=1, status=0):
	if username == '' or password == '':
		return False, u'用户名与密码不能为空'

	_user = get_user_by_username(username)
	if _user:
		return False, u'用户已存在'

	if not str(age).isdigit() or int(age) < 0 or int(age) > 100:
		return False, u'用户年龄不正确'

	return True, ''

# 添加用户信息
def add_user(username, password, telephone, age, sex=1, status=0):
	_user = get_user_by_username(username)
	if _user is None:
		_cnt, _ = execute_sql(SQL_INSERT, (username, password, telephone, age,sex, status))
		return _cnt > 0
	return False

# 验证用户在更新信息是否正确
def validate_user_modify(telephone, age, sex=1, status=0):
	if not str(age).isdigit() or int(age) < 0 or int(age) > 100:
		return False, u'用户年龄不正确'
	return True, ''

# 更改用户信息
def modify_user(uid, telephone, age, sex=1, status=0):
	_cnt, _ = execute_sql(SQL_MODIFY, (telephone, age, sex, status, uid))
	return True

# 根据用户主键删除用户信息
def delete_user(uid):
	_cnt, _ = execute_sql(SQL_DELETE_BY_ID, (uid,))
	return _cnt > 0

# 获取机房信息
def get_machine_room():
	_cnt, _machines = execute_sql(SQL_FETCH_MACHINE_ROOM, (), is_fetch=True)
	return dict(_machines)

# 获取所用资产的信息
def get_assets(query=''):
	if query == '':
		_cnt, _assets = execute_sql(SQL_FETCH_ASSET_ALL, (), True)
	else:
		_cnt, _assets = execute_sql(SQL_FETCH_ASSET_BY_SN,('%%%s%%' % query,), True)
	return [dict(zip(COLUMN_ASSET, _asset)) for _asset in _assets]

# 根据资产主键获取资产的信息
def get_asset_by_id(uid):
	_cnt, _assets = execute_sql(SQL_GET_ASSET_BY_ID, (uid,), True)
	return dict(zip(COLUMN_ASSET, _assets[0])) if _cnt > 0 else None

# 根据SN获取资产的信息
def get_asset_by_sn(sn):
	_cnt, _assets = execute_sql(SQL_GET_ASSET_BY_SN, (sn,), True)
	return dict(zip(COLUMN_ASSET, _assets[0])) if _cnt > 0 else None

# 验证资产添加信息是否正确
def validate_asset_add(sn, vendor, machine_room_id, model, purchase_date, cpu, ram, disk, os, ip, hostname, admin, business):
	_asset = get_asset_by_sn(sn)
	if _asset:
		return False, u'资产已存在'

	if not str(cpu).isdigit() or int(cpu) < 1 or int(cpu) > 80:
		return False, u'cpu填写错误'

	return True, ''

# 添加资产信息
def add_asset(sn, vendor, machine_room_id, model, purchase_date, cpu, ram, disk, os, ip, hostname, admin, business):
	_asset = get_asset_by_sn(sn)
	if _asset is None:
		_cnt, _ = execute_sql(SQL_ASSET_INSERT, (sn, vendor, machine_room_id, model, purchase_date, cpu, ram, disk, os, ip, hostname, admin, business))
		return _cnt > 0
	return False


# 验证资产在更新信息是否正确
def validate_asset_modify(cpu, ram, disk, status=0):
	if not str(cpu).isdigit() or int(age) < 1 or int(age) > 80:
		return False, u'cpu填写错误'
	if not str(ram).isdigit():
		return False, u'内存填写错误'
	if not str(disk).isdigit():
		return False, u'硬盘填写错误'
	return True, ''

# 更改资产信息
def modify_asset(uid, cpu, ram, disk, status=0):
	_cnt, _ = execute_sql(SQL_ASSET_MODIFY, (cpu, ram, disk, status, uid))
	return True

# 根据资产主键删除资产信息
def delete_asset(uid):
	_cnt, _ = execute_sql(SQL_DELETE_ASSET_BY_ID, (uid,))
	return _cnt > 0

if __name__ == '__main__':
	#print get_users()
	#print get_user_by_username('sherry')
	#print get_user_by_id(3)
	#print validate_user_add('user3', '123456', '', 'abc')
	#print validate_user_add('user2', '123456', '', '12.4')
	#print validate_user_add('user1', '123456', '', '25')
	#print add_user('guanyu', '123456', '22345687998', 24)
	#print add_user('zhangfei', '123456', '12345687100', 23)
	#print validate_user_login('zhaoyun', '1234')
	#print get_machine_room()
	print get_assets()
	#pass