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
class User(object):
    columns = ['id', 'username', 'password', 'telephone', 'age', 'sex', 'status']
    sql_login = 'SELECT * FROM user WHERE username=%s AND password=md5(%s) LIMIT 1;'
    sql_fetch_all = 'SELECT %s FROM user'
    sql_fetch_count = 'SELECT count(*) FROM user'
    sql_get_by_username = 'SELECT %s FROM user WHERE username=%%s LIMIT 1;'
    sql_insert = 'INSERT INTO user(username, password, telephone, age, sex, status) VALUES(%s, md5(%s), %s, %s, %s, %s);'
    sql_get_by_key = 'SELECT %s FROM user WHERE id=%%s LIMIT 1;'
    sql_modify = 'UPDATE user SET telephone=%s, age=%s WHERE id=%s;'
    sql_delete_by_key = 'DELETE FROM user WHERE id=%s;'

    def __init__(self, user):
        self.id = user.get('id', '')
        self.username = user.get('username', '')
        self.password = user.get('password', '')
        self.telephone = user.get('telephone', '')
        self.sex = user.get('sex', 1)
        self.age = user.get('age', 0)
        self.status = user.get('status', 0)

    def login(self):
        _cnt, _ = execute_sql(self.sql_login, (self.username, self.password), True)
        return _cnt > 0

    @classmethod
    def fetch_count(cls, query=''):
        _sql = cls.sql_fetch_count
        _args = []
        if query.strip() != '':
            _sql += ' WHERE username like %s'
            _args.append('%' + query + '%')
        _cnt, _ret = execute_sql(_sql, _args, True)
        return _ret[0][0] if _cnt > 0 else 0 

    @classmethod
    def fetch_all(cls, query='', offset=None, limit=None):
        _sql = cls.sql_fetch_all % ','.join(cls.columns)
        _args = []
        if query.strip() != '':
            _sql += ' WHERE username like %s'
            _args.append('%' + query + '%') # '%%%s%%' % (query, )
        
        if limit is not None:
            _sql += ' LIMIT %s'
            _args.append(limit)

        if offset is not None:
            _sql += ' OFFSET %s'
            _args.append(offset)

        print _sql
        _cnt, _users = execute_sql(_sql, _args, True)
        return [User(dict(zip(cls.columns, _user))) for _user in _users]

    def validate_add(self):
        if self.username == '' or self.password == '':
            return False, '用户名和密码不能为空'

        _user = self.get_by_username(self.username)
        if _user is not None:
            return False, '用户已注册'

        if not str(self.age).isdigit() or int(self.age) < 0 or int(self.age) > 100:
            return False, '用户年龄不正确'

        return True, ''

    @classmethod
    def get_by_username(cls, username):
        _sql = cls.sql_get_by_username % ','.join(cls.columns)
        _cnt, _users = execute_sql(_sql, (username, ), True)
        return dict(zip(cls.columns, _users[0])) if _cnt > 0 else None

    def create(self):
        _user = self.get_by_username(self.username)
        if _user is None:
            _cnt, _ = execute_sql(self.sql_insert, \
                (self.username, self.password, self.telephone, self.age, self.sex, self.status))
            return _cnt > 0
        return False

    @classmethod
    def get_by_key(cls, key):
        _sql = cls.sql_get_by_key % ','.join(cls.columns)
        _cnt, _users = execute_sql(_sql, (key, ), True)
        return User(dict(zip(cls.columns, _users[0]))) if _cnt > 0 else None

    def validate_modify(self):
        if not str(self.age).isdigit() or int(self.age) < 0 or int(self.age) > 100:
            return False, '用户年龄不正确'
        return True, ''

    def update(self):
        _cnt, _ = execute_sql(self.sql_modify, (self.telephone, self.age, self.id))
        return True 

    @classmethod
    def delete(cls, key):
        _cnt, _ = execute_sql(cls.sql_delete_by_key, (key,))
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
