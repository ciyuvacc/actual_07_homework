#coding=utf-8
import MySQLdb as mysql
import dbconf
#from logshow import *

#def connect_mysql():
#    return mysql.connect(host=dbconf.DBHOST,port=dbconf.DBPORT,user=dbconf.DBUSER,db=dbconf.DBNAME,charset=dbconf.DBCHARSET)

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

#添加用户
add_user_sql = 'insert into accout (username,password,email,createtime) values(%s,md5(%s),%s,now());'

#判断用户是否存在
exist_user_sql = 'select * from accout where username=%s or email=%s;'

#验证用户登录
auth_user_sql = 'select * from accout where username=%s and password=md5(%s);'

# 获取用户列表
get_user_sql = 'select * from accout;'
get_user_sql_by_name = 'select * from accout where username LIKE %s;'

# 更改用户
modify_user_sql = 'update accout set password=md5(%s),email=%s where id=%s;'

# 删除用户
delete_user_sql = 'delete from accout where username=%s;'

# 日志入库
get_log_sql = "insert nginx_log values (%s,%s,%s,%s);"

# 展示日志
show_log_sql = 'select * from nginx_log order by count desc limit %s;'

# 添加主机
add_host_sql = 'insert into hosts (hostname,ip,lanip,memory,disk,cpu,os,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);'

# 获取主机
get_hostlist_sql = 'select * FROM hosts;'
get_hostlist_sql_by_hostname = 'select * FROM hosts WHERE  hostname LIKE %s;'

# 更新主机信息
update_host_sql = 'update hosts SET hostname=%s,ip=%s,lanip=%s,memory=%s,disk=%s,cpu=%s,os=%s WHERE id=%s;'

# 删除主机信息
del_host_sql = 'delete FROM hosts WHERE id=%s AND hostname=%s;'


def exist_user(username,email=""):
    count, _ = Exect_sql(exist_user_sql,(username,email))
    return count == 0

def add_user(username,password,email):
    count, _ = Exect_sql(add_user_sql,(username,password,email))
    return count > 0

def auth_user(username,password):
    count, _ = Exect_sql(auth_user_sql,(username,password))
    return count > 0

def get_user(selectuser=""):
    dict_user = ['id','username','password','email','create_time']
    if selectuser == "":
        count, users = Exect_sql(get_user_sql,(),True)
    else:
        count, users = Exect_sql(get_user_sql_by_name,('%'+ selectuser,),True)
    return  [dict(zip(dict_user,user)) for user in users]

def modify_user(password,email,id):
    count, _ = Exect_sql(modify_user_sql,(password,email,int(id)))
    return True

def delete_user(username):
    count, _ = Exect_sql(delete_user_sql,(username))
    return count > 0

def show_log(numbers=10):
    count, logs = Exect_sql(show_log_sql,int(numbers))
    return logs

def add_host(hostname,hostip,hostlanip,hostmemory,hostdisk,hostcpu,hostos,hoststatus):
    count,_ = Exect_sql(add_host_sql,(hostname,hostip,hostlanip,hostmemory,hostdisk,hostcpu,hostos,hoststatus))
    return count > 0

def get_hostlist(hostname=""):
    dict_host = ['id','hostname','ip','lanip','memory','disk','cpu','os','status']
    if hostname == "":
        count, hosts = Exect_sql(get_hostlist_sql,(),True)
    else:
        count, hosts = Exect_sql(get_hostlist_sql_by_hostname,('%'+ hostname,),True)
    return [dict(zip(dict_host,host)) for host in hosts]

def updatehost(hostname,hostip,hostlanip,hostmemory,hostdisk,hostcpu,hostos,hostid):
    count, _ = Exect_sql(update_host_sql,(hostname,hostip,hostlanip,hostmemory,hostdisk,hostcpu,hostos,hostid))
    return count > 0

def del_host(hostid,hostname):
    count, _ = Exect_sql(del_host_sql,(hostid,hostname))
    return count > 0


'''
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
        print users
    else:
        count = cur.execute("select * from accout where username=%s;",(selectuser,))
        users = cur.fetchall()
        print users
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
'''

def get_log():
    conn = connect_mysql()
    cur = conn.cursor()
    for s in _list:
        sql = 'insert  nginx_log values(%s,%s,%s,%s)' % s
        count = cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
'''
def show_log(numbers=10):
    conn = connect_mysql()
    cur = conn.cursor()
    count = cur.execute('select * from nginx_log order by count desc limit %s ;',int(numbers))
    logs = cur.fetchall()
    cur.close()
    conn.close()
    return logs


def addhost(hostname,hostip,hostlanip,hostmemory,hostdisk,hostcpu,hostos,hoststatus):
    conn = connect_mysql()
    cur = conn.cursor()
    count = cur.execute('insert into hosts (hostname,ip,lanip,memory,disk,cpu,os,status) VALUES (%s,%s,%s,%d,%d,%d,%s,%s);',(hostname,hostip,hostlanip,hostmemory,hostdisk,hostcpu,hostos,hoststatus))
    conn.commit()
    cur.close()
    conn.close()
    return count > 0
'''





