#encoding: utf-8

USER_FILE_PATH = 'user.txt'
FILE_CONTENT_DICT = {0 : 'username', 1 : 'password', 2 : 'telephone', 3 : 'sex'}

# 获取所有用户的信息
# 格式{username: {username: "", password: "", telephone: ""}}
def get_users():
    _user_dict = {}
    try:
        handle = open(USER_FILE_PATH, 'rb')
        for line in handle:
            _nodes = line.split()
            _user = {}
            for _idx in range(len(_nodes)):
                _user[FILE_CONTENT_DICT.get(_idx)] = _nodes[_idx]
            _user_dict[_user.get('username')] = _user
        handle.close()
    except BaseException as e:
        print str(e)    
    return _user_dict


# 根据username获取用户的信息
def get_user(username):
    _users = get_users()
    return _users.get(username)


# 验证用户登陆时信息是否正确
def validate_user_login(username, password):
    _user = get_user(username)
    return (not not _user) and _user.get('password') == password


# 验证用户在添加信息是否正确
def validate_user_add(username, password, telephone):
    if username == '' or password == '':
        return False, '用户名和密码不能为空'

    _user = get_user(username)
    if _user is not None:
        return False, '用户已注册'

    return True, ''


# 添加用户信息(若用户名已存在则不添加)
def add_user(username, password, telephone):
    _user = get_user(username)
    if _user is None:
        handle = open(USER_FILE_PATH, 'ab')
        handle.write('%s %s %s\n' % (username, password, telephone))
        handle.close()
        return True
    return False


# 测试的代码
if __name__ == '__main__':
    print get_users()
    print get_user('woniu')
    print validate_user('pc', '123')
    print validate_user('woniu', '123')
    print validate_user('woniu', '123456')
    print add_user('test', '123456', '12345687998')