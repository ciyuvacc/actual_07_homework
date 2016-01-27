#encoding: utf-8
import MySQLdb
import config

def get_conn():
    conn=MySQLdb.connect(host=config.DB_HOST,user=config.DB_USER,passwd=config.DB_PASSWD,db=config.DB_DATABASE,charset=config.DB_CHARSET)
    conn.autocommit(1)
    cursor = conn.cursor()
    return cursor

# #创建用户表
# sql = "create table if not exists user(id INT(10) not null  auto_increment,username varchar(30),password varchar(30),telephone INT (11),address VARCHAR (30),primary key(id))"
# cursor.execute(sql)
# #写入测试数据
# sql = "insert into user(username,password,telephone,address) values(%s,%s,%d,%s)"
# param = (("xuheng","xuheng123",13336181920,"hangzhou"),("wangwang","wang123",13336181921,"hangzhou"))
# n = cursor.executemany(sql,param)
# print 'insertmany',



# 获取所有用户的信息
# 格式{username: {username: "", password: "", telephone: ""}}
def get_users():
    _user_dict = {}
    cursor = get_conn()
    sql = "select username,password,telephone,address from user"
    n = cursor.execute(sql)
    for row in cursor.fetchall():
        _user_dict[row[0]]={'username':row[0],'password':row[1],'telephone':row[2]}
    cursor.close()
    return _user_dict

# 根据username获取用户的信息
def get_user(username):
    _user_dict = {}
    cursor = get_conn()
    n = cursor.execute('select username,password,telephone from user where username="'+username+'"')
    row=cursor.fetchone()
    _user_dict[row[0]]={'username':row[0],'password':row[1],'telephone':row[2]}
    cursor.close()
    return _user_dict.get(username)

# 根据username删除用户的信息
def del_user(username):
    cursor = get_conn()
    n = cursor.execute('delete from user where username="'+username+'"')
    cursor.close()
    return n

# 验证用户登陆时信息是否正确
def validate_user_login(username, password):
    cursor = get_conn()
    n = cursor.execute('select username,password from user where username="'+username+'"'+' and password="'+password+'"')
    cursor.close()
    return n

# 验证用户在添加信息是否正确
def validate_user_add(username, password, telephone):
    if username == '' or password == '':
        return False, '用户名和密码不能为空'
    cursor = get_conn()
    n = cursor.execute('select username from user where username="'+username+'"')
    cursor.close()
    if n:
        return False, '用户已注册'
    else:
        return True, ''


#检查手机号
def validate_user_phone(telephone):
        phone_fix=['130','131','132','133','134','135','136','137','138','139','150','151','152','153','156','158','159','170','183','182','185','186','188','189']
        if len(telephone)<>11:
                return False,"手机号码为11位"
        else:
                if  telephone.isdigit():
                        if telephone[:3] in phone_fix:
                                return True,''
                        else:
                                return False,"手机号码无效"
                else:
                        return False,"手机号码为整数，请检查"


# 添加用户信息(若用户名已存在则不添加)
def add_user(username, password, telephone):
    cursor = get_conn()
    sql = "insert into user(username,password,telephone,address) values(%s,%s,%s,%s)"
    param = (username,password,telephone,'hangzhou')
    n = cursor.execute(sql,param)
    cursor.close()
    if n:
        return True
    else:
        return False

#更新用户信息
def updata_user(username, password, telephone):
    cursor = get_conn()
    sql = "update user set password=%s,telephone=%s where username=%s "
    param = (password,telephone,username)
    print param
    n = cursor.execute(sql,param)
    print n
    cursor.close()
    if n:
        return True
    else:
        return False





# 测试的代码
if __name__ == '__main__':
    print add_user('lisi','lisi123','13336181920')
    print validate_user_add('lisi','lisi123','13336181920')
    print validate_user_login('lisi','lisi123')
    print updata_user('lisi','lisi123','13333333')
    print get_user('lisi')
    print del_user('lisi')

