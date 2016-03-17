#coding=utf-8
import MySQLdb as mysql
import dbconf
from logshow import *



def Exect_sql(sql,args,is_fetch=False):
    conn, cur = None,None
    count, rtn_fetch = 0,()
    try:
        conn = mysql.connect(host=dbconf.DBHOST,port=dbconf.DBPORT,user=dbconf.DBUSER,db=dbconf.DBNAME,charset=dbconf.DBCHARSET)
        cur = conn.cursor()
        count = cur.execute(sql,args)
        if is_fetch:
            rtn_fetch = cur.fetchall()
        else:
            conn.commit()
    except BaseException, e:
        print str(e)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    return count, rtn_fetch

# 日志入库
get_log_sql = "insert nginx_log values (%s,%s,%s,%s);"

# 展示日志
show_log_sql = 'select * from nginx_log order by count desc limit %s;'


def show_log(numbers=10):
    count, logs = Exect_sql(show_log_sql,int(numbers))
    return logs


class User(object):
    dict_user = ['id','username','password','email','create_time']
    #添加用户
    add_user_sql = 'insert into accout (username,password,email,createtime) values(%s,md5(%s),%s,now())'
    #判断用户是否存在
    exist_user_sql = 'select * from accout where username=%s OR email=%s'
    #验证用户登录
    auth_user_sql = 'select * from accout where username=%s and password=md5(%s)'
    # 获取用户列表
    get_user_sql = 'select * from accout'
    # 用户数
    fetch_all_sql = 'select count(1) from accout'
    # 更改用户
    modify_user_sql = 'update accout set password=md5(%s),email=%s where id=%s'
    # 删除用户
    delete_user_sql = 'delete from accout where username=%s'

    def __init__(self,user):
        self.id=user.get('id','')
        self.username = user.get('username','')
        self.password = user.get('password','')
        self.email = user.get('email','')
        self.create_time = user.get('create_time','')

    def auth_user(self):
        count, _ = Exect_sql(self.auth_user_sql,(self.username,self.password),True)
        return count > 0

    def exist_user(self):
        count, _ = Exect_sql(self.exist_user_sql,(self.username,self.email))
        return count == 0

    @classmethod
    def fetch_all(cls,query=''):
        _sql = cls.fetch_all_sql
        _args = []
        if query.strip() != '':
            _sql += ' where username like %s;'
            _args.append('%' + query + '%')
        count,result = Exect_sql(_sql,_args,True)
        return result[0][0] if count > 0 else 0

    @classmethod
    def all_users(cls,query='',offset=None,limit=None):
        _sql = cls.get_user_sql
        _args = []
        if query.strip() != '':
            _sql += ' where username like %s'
            _args.append('%' + query + '%')
        if limit is not None:
            _sql += ' limit %s'
            _args.append(limit)
        if offset is not None:
            _sql += ' offset %s'
            _args.append(offset)
        print _sql
        count, users = Exect_sql(_sql,_args,True)
        return [User(dict(zip(cls.dict_user,user))) for user in users]

    def add_user(self):
        count , _ = Exect_sql(self.add_user_sql,(self.username,self.password,self.email))
        return count > 0

    def modify_user(self):
        count, _ = Exect_sql(self.modify_user_sql,(self.password,self.email,self.id))
        return count > 0

    def delete_user(self):
        count ,_ =Exect_sql(self.delete_user_sql,(self.username))
        return count > 0


# 主机管理
class Host(object):
    dict_host = ['id','hostname','ip','lanip','memory','disk','cpu','os','status']
    # 添加主机
    add_host_sql = 'insert into hosts (hostname,ip,lanip,memory,disk,cpu,os,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    # 获取主机
    get_hostlist_sql = 'select * FROM hosts'
    # 主机数
    fetch_all_host_sql = 'select count(1) from hosts'
    # 更新主机信息
    update_host_sql = 'update hosts SET hostname=%s,ip=%s,lanip=%s,memory=%s,disk=%s,cpu=%s,os=%s WHERE id=%s'
    # 删除主机信息
    del_host_sql = 'delete FROM hosts WHERE id=%s AND hostname=%s'

    def __init__(self,host):
        self.id = host.get('id','')
        self.hostname = host.get('hostname','')
        self.ip = host.get('ip','')
        self.lanip = host.get('lanip','')
        self.memory = host.get('memory','')
        self.disk = host.get('disk','')
        self.cpu = host.get('cpu','')
        self.os = host.get('os','')
        self.status = host.get('status','')

    def add_host(self):
        count , _ = Exect_sql(self.add_host_sql,(self.hostname,self.ip,self.lanip,self.memory,self.disk,self.cpu,self.os,self.status))
        return count > 0

    @classmethod
    def fetch_all_host(cls,query=''):
        _sql = cls.fetch_all_host_sql
        _args = []
        if query.strip() != '':
            _sql += ' where hostname like %s;'
            _args.append('%' + query + '%')
        count,result = Exect_sql(_sql,_args,True)
        return result[0][0] if count > 0 else 0

    @classmethod
    def get_hostlist(cls,query='',limit=None,offset=None):
        _sql = cls.get_hostlist_sql
        _args = []
        if query.strip() != '':
            _sql += ' where hostname like %s'
            _args.append('%' + query + '%')
        if limit is not None:
            _sql += ' limit %s'
            _args.append(limit)
        if offset is not None:
            _sql += ' offset %s'
            _args.append(offset)
        count ,hosts = Exect_sql(_sql,_args,True)
        return [Host(dict(zip(cls.dict_host,host))) for host in hosts]

    def del_host(self):
        count,_ = Exect_sql(self.del_host_sql,(self.id,self.hostname))
        return count > 0

    def updatehost(self):
        count , _ = Exect_sql(self.update_host_sql,(self.hostname,self.ip,self.lanip,self.memory,self.disk,self.cpu,self.os,self.id))
        return count > 0















