#encoding: utf-8

from dbutil import execute_sql

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

# table中定义的用户属性
COLUMS_USER = ['id', 'username', 'password', 'telephone', 'age', 'sex', 'status']

# 查询所有用户sql语句
SQL_FETCH_ALL = 'SELECT %s FROM user;' % ', '.join(COLUMS_USER)

# 根据用户名查询用户信息sql语句
SQL_FETCH_BY_USERNAME = 'SELECT %s FROM user WHERE username like %%s;' % ', '.join(COLUMS_USER)

# 根据用户主键获取用户信息sql语句
SQL_GET_BY_ID = 'SELECT %s FROM user WHERE id=%%s LIMIT 1;' % ', '.join(COLUMS_USER)

# 根据用户名获取用户信息sql语句
SQL_GET_BY_USERNAME = 'SELECT %s FROM user WHERE username=%%s LIMIT 1;' % ', '.join(COLUMS_USER)

# 根据用户名密码查询用户信息数量sql语句
SQL_VALIDATE_LOGIN = 'SELECT * FROM user WHERE username=%s AND password=md5(%s) LIMIT 1;'

# 添加用户信息
SQL_INSERT = 'INSERT INTO user(username, password, telephone, age, sex, status) VALUES(%s, md5(%s), %s, %s, %s, %s);'

# 更新用户信息
SQL_MODIFY = 'UPDATE user SET telephone=%s, age=%s, sex=%s, status=%s WHERE id=%s;'

# 根据用户主键ID删除用户
SQL_DELETE_BY_ID = 'DELETE FROM user WHERE id=%s;'

# 获取所有用户的信息
# 格式[{id: "", username: "", password: "", telephone: "", age: "", sex: "", status: ""}]
def get_users(query=''):
    if query == '':
        _cnt, _users = execute_sql(SQL_FETCH_ALL, (), True)
    else:
        _cnt, _users = execute_sql(SQL_FETCH_BY_USERNAME, ('%%%s%%' % query,), True)
    return [dict(zip(COLUMS_USER, _user)) for _user in _users]


# 根据用户主键获取用户的信息
def get_user_by_id(uid):
    _cnt, _users = execute_sql(SQL_GET_BY_ID, (uid, ), True)
    return dict(zip(COLUMS_USER, _users[0])) if _cnt > 0 else None


# 根据username获取用户的信息
def get_user_by_username(username):
    _cnt, _users = execute_sql(SQL_GET_BY_USERNAME, (username, ), True)
    return dict(zip(COLUMS_USER, _users[0])) if _cnt > 0 else None


# 验证用户登陆时信息是否正确
def validate_user_login(username, password):
    _cnt, _ = execute_sql(SQL_VALIDATE_LOGIN, (username, password), True)
    return _cnt > 0

# 验证用户在添加信息是否正确
def validate_user_add(username, password, telephone, age, sex=1, status=0):
    if username == '' or password == '':
        return False, '用户名和密码不能为空'

    _user = get_user_by_username(username)
    if _user is not None:
        return False, '用户已注册'

    if not str(age).isdigit() or int(age) < 0 or int(age) > 100:
        return False, '用户年龄不正确'

    return True, ''


# 添加用户信息(若用户名已存在则不添加)
def add_user(username, password, telephone, age, sex=1, status=0):
    _user = get_user_by_username(username)
    if _user is None:
        _cnt, _ = execute_sql(SQL_INSERT, (username, password, telephone, age, sex, status))
        return _cnt > 0
    return False


# 验证用户在更新信息是否正确
def validate_user_modify(telephone, age, sex=1, status=0):
    if not str(age).isdigit() or int(age) < 0 or int(age) > 100:
        return False, '用户年龄不正确'
        
    return True, ''

# 更改用户信息
def modify_user(uid, telephone, age, sex=1, status=0):
    _cnt, _ = execute_sql(SQL_MODIFY, (telephone, age, sex, status, uid))
    return True 


# 根据用户主键删除用户信息
def delete_user(uid):
    _cnt, _ = execute_sql(SQL_DELETE_BY_ID, (uid,))
    return _cnt > 0

COLUMS_MACHINE_ROOMS = ['id', 'name']

SQL_FETCH_ALL_MACHINE_ROOM = 'SELECT %s FROM machine_room;' % ','.join(COLUMS_MACHINE_ROOMS)

# 获取所有机房信息
def get_machine_rooms():
    _, _machine_rooms = execute_sql(SQL_FETCH_ALL_MACHINE_ROOM, (), True)
    return dict(_machine_rooms)

COLUMS_ASSET = 'id,sn,vendor,machine_room_id,model,purchase_date,cpu,ram,disk,os,ip,hostname,admin,bussiness,status'.split(',')

COLUMNS_ADD_ASSET = 'sn,vendor,machine_room_id,model,purchase_date,cpu,ram,disk,os,ip,hostname,admin,bussiness'.split(',')

SQL_FETCH_ALL_ASSET = 'SELECT %s FROM asset' % ','.join(COLUMS_ASSET)

SQL_COUNT_ASSET = 'SELECT count(*) FROM asset;'


# 获取所有资产的数量
def get_asset_count():
    _, _cnt = execute_sql(SQL_COUNT_ASSET, (), True)
    return _cnt[0][0] if _cnt is not None and len(_cnt) > 0 else 0

# 获取所有资产信息
def get_assets(query='', offset=None, limit=None):
    _machine_rooms = get_machine_rooms()
    _sql = SQL_FETCH_ALL_ASSET
    _args = []
    if query != '':
        _sql += ' WHERE hostname like %s '
        _args.append('%%%s%%' % query)

    if limit is not None:
        _sql += ' LIMIT %s'
        _args.append(limit)

    if offset is not None:
        _sql += ' OFFSET %s'
        _args.append(offset)
        
    _cnt, _assets = execute_sql(_sql, _args, True)
    return [dict(zip(COLUMS_ASSET, _asset)) for _asset in _assets]

def create_asset_obj(req):
    _obj = {}
    for column in COLUMNS_ADD_ASSET:
        _obj[column] = req.get(column, '')
    return _obj

def validate_asset_add(obj):
    errors = {}
    result = ''
    for key, value in obj.items():
        if value.strip() == '':
            result = '验证失败'
            errors[key] = '不能为空'

    return len(errors) == 0, result, errors

def add_asset(obj):
    _args = []
    for column in COLUMNS_ADD_ASSET:
        _args.append(obj.get(column, ''))
    _sql = 'insert into asset(%s) VALUES(%s);' % (','.join(COLUMNS_ADD_ASSET), ','.join(['%s'] * len(COLUMNS_ADD_ASSET)))
    _cnt, _ = execute_sql(_sql, _args)
    return _cnt > 0

# 测试的代码
if __name__ == '__main__':
    print get_users()
    print get_user_by_username('woniu')
    print validate_user_add('pc', '123', '', 'abc')
    print validate_user_add('woniu', '123', '', '12.4')
    print validate_user_add('woniu', '123456', '', '45')
    print add_user('test', '123456', '12345687998', 24)
    print add_user('kk', '123456', '12345687998', 13)
