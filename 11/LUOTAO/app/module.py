#coding:utf-8
#base module
from . import app
import math
import hashlib
import time
import paramiko
#import logging
import traceback



#logger = logging.getLogger(__name__)

from functools import wraps
from flask import session,redirect

def login_required(func):
    @wraps(func)
    def wapper(*args,**kwargs):
        if session.get('username') is None:
            return redirect('/')
        rtn = func(*args,**kwargs)
        return rtn 
    return wapper

def md5_str(s):
     md5 = hashlib.md5()
     md5.update(s)
     return md5.hexdigest()

def paging(total,nowpage,pagesize):
    print total ,nowpage,pagesize
    pagesize = int(pagesize) if str(pagesize).isdigit() else pagesize
    max_page_num = int(math.ceil(total * 1.0 / pagesize))
    nowpage = 1 if nowpage < 1 or nowpage > max_page_num else nowpage
    nextpage = 0 if total ==0 else nowpage + 1
    lastpage = nowpage - 1
    if max_page_num >5:
        startpage =1 if nowpage -2 <0 else nowpage -2
        if nowpage +2 > total:
            endpage = total
            startpage = total - 4
        else:
            endpage = nowpage +2
    else:
        startpage=1
        endpage =max_page_num
    pagedata={"nextpage":nextpage,"lastpage":lastpage,"nowpage":nowpage,"maxpage":max_page_num,"endpage":endpage,"startpage":startpage}
    return pagedata


class User(object):
    colums = ['username','password','age','sex','address','email']
    tablename = "user"
    sql_fetch_all = 'select %s from %s'
    sql_insert = 'INSERT INTO %s VALUES(%s)'
    sql_update = 'UPDATE %s SET %s WHERE %s'
    sql_delete = 'DELETE FROM %s WHERE %s'
    
    def __init__(self,user):
        self.username = user.get('username','').encode("utf-8")
        self.password = md5_str(user.get('password','').encode("utf-8"))
        self.age = int(user.get('age','0').encode("utf-8"))
        self.sex = int(user.get('sex','1').encode("utf-8"))
        self.address = user.get('address','').encode("utf-8")
        self.email = user.get('email','').encode("utf-8")
          
      
    def _login(self):
        sql_login = self.sql_fetch_all % ('username,password',self.tablename+'  ' +'where username=%s AND password=%s limit 1' )
        tmp = app.config['cursor']._execute(sql_login,(self.username,self.password,))
        cur=tmp['cur'].fetchall()
        if cur != ():
            return True
           
    def _sign(self):
        sql_Verify_user = self.sql_fetch_all % ('username',self.tablename+'  ' +'where username=%s limit 1' )
        print sql_Verify_user,(self.username,)
        tmp = app.config['cursor']._execute(sql_Verify_user,(self.username,))
        cur=tmp['cur'].fetchall()
        if cur == ():            
            sql_sign = self.sql_insert % (self.tablename +'('+','.join(self.colums)+')',' %s, %s, %s, %s, %s, %s')
            print sql_sign,(self.username,self.password,self.age,self.sex,self.address,self.email,)
            tmp = app.config['cursor']._execute(sql_sign,(self.username,self.password,self.age,self.sex,self.address,self.email,))
            cur=tmp['cur'].fetchall() 
            return tmp['msg']
        else:
            return 'error'          
           
    def _changeuser(self):
        sql_change =  self.sql_update % (self.tablename , 'password=md5(%s) , age=%s  , address=%s , email=%s' , 'username=%s')
        print sql_change,(self.password,self.age,self.address,self.email,self.username,)
        tmp = app.config['cursor']._execute(sql_change,(self.password,self.age,self.address,self.email,self.username,))
        cur=tmp['cur'].fetchall()
        return tmp['msg']


          
    def _deluser(self):
        sql_delete_user = self.sql_delete % (self.tablename , 'username=%s')
        print sql_delete_user,(self.username,)
        tmp = app.config['cursor']._execute(sql_delete_user,(self.username,))
        cur=tmp['cur'].fetchall()
        return tmp['msg']


    @classmethod
    def _page(cls,nowpage,pagesize,query):
        if query != '':
            query = '  WHERE username like "%%%s%%"' % ('%'+ query+'%', )
        sql_query  = cls.sql_fetch_all % (','.join(cls.colums),cls.tablename + query + '  limit %s, %s')
        sql_select_count = cls.sql_fetch_all % ('count(*)',cls.tablename + query)

        tmp = app.config['cursor']._execute(sql_select_count,())
        cur=tmp['cur'].fetchall()

        total=0 if cur == () else cur[0][0]
        data_list= paging(total,nowpage,pagesize)

        start_position = (data_list['nowpage'] - 1) * pagesize
        tmp1 = app.config['cursor']._execute(sql_query,(start_position,  pagesize,))
        data_list['data']= tmp1['cur'].fetchall() 

        return data_list


class Server(object):
    colums = ["id","sn","ip","servername","idc","operation","user","cpu","memery","disk","system","model","buy_date","producter"]
    tablename = "server02"
    sql_fetch_all = 'select %s from %s'
    sql_insert = 'INSERT INTO %s VALUES(%s)'
    sql_update = 'UPDATE %s SET %s WHERE %s'
    sql_delete = 'DELETE FROM %s WHERE %s'
    
    def __init__(self,server):            
        self.id = server.get('id','').encode('utf-8')
        self.sn = server.get('sn','').encode('utf-8')
        self.ip = server.get('ip','').encode('utf-8')
        self.servername = server.get('servername','').encode('utf-8')
        self.idc = server.get('idc','').encode('utf-8')
        self.operation = server.get('operation','').encode('utf-8')
        self.user = server.get('user','').encode('utf-8')
        self.cpu = server.get('cpu','').encode('utf-8')
        self.memery = server.get('memery','').encode('utf-8')
        self.disk = server.get('disk','').encode('utf-8')
        self.system = server.get('system','').encode('utf-8')
        self.model = server.get('model','').encode('utf-8')
        self.buy_date = server.get('buy_date','').encode('utf-8')
        self.producter = server.get('producter','').encode('utf-8')

    @classmethod
    def _select(cls,nowpage,pagesize,query):
        if query != '':
            query = '  WHERE ip like "%%%s%%"' % ('%'+ query+'%', )
        sql_query  = cls.sql_fetch_all % (','.join(cls.colums),cls.tablename + query + '  limit %s, %s')
        sql_select_count = cls.sql_fetch_all % ('count(*)',cls.tablename + query)

        tmp = app.config['cursor']._execute(sql_select_count,())
        cur=tmp['cur'].fetchall()

        total=0 if cur == () else cur[0][0]
        data_list= paging(total,nowpage,pagesize)

        start_position = (data_list['nowpage'] - 1) * pagesize
        tmp1 = app.config['cursor']._execute(sql_query,(start_position,  pagesize,))
        data_list['data']= tmp1['cur'].fetchall() 

        return data_list

   
class Monitor(object):
    def  __init__(self,ip,mtime,cpu,mem):
        self.ip = ip
        self.mtime = mtime
        self.cpu = cpu
        self.mem = mem
    def save(self):
        _sql = 'insert into monitor(ip,mtime,cpu,mem)values(%s,%s,%s,%s)'
        #print _sql,(self.ip,self.mtime,self.cpu,self.mem)
        tmp = app.config['cursor']._execute(_sql,(self.ip,self.mtime,self.cpu,self.mem))
        data= tmp['cur'].fetchall()
        return data

    @classmethod
    def getData(cls, ip):
        _sql = 'select * from monitor where ip = %s and mtime >= %s order by mtime asc'
        mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - 60 * 60))
        print _sql,(ip, mtime)
        tmp = app.config['cursor']._execute(_sql,(ip, mtime))
        _res= tmp['cur'].fetchall()
        print _res
        print '00000000'
        _times = []
        _cpu_data = [] 
        _mem_data = []
        for _rs in _res:
            _cpu, _mem, _time = _rs[2], _rs[3], _rs[4]          
            _times.append(_time.strftime('%H:%M'))
            _cpu_data.append(_cpu)
            _mem_data.append(_mem)
        return {'categories' : _times, 'series' : [{'name' : 'CPU', 'data' : _cpu_data}, {'name' : '内存', 'data' : _mem_data}]}
        
class SshConnect(object):
    def  __init__(self,ip,username,port):
        self.ip = ip
        self.username = username
        self.port = port

    def pass_connect(self, pwd, commands=[]):
        ssh = None 
        data = {}
        data['cmd']={}
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip, self.port, self.username, pwd)
            print self.ip, self.port, self.username, pwd
            for cmd in commands:
                #logger.info('exec %s', cmd)
                print 'exec %s' % cmd
                stdin, stdout, stderr = ssh.exec_command(cmd)
                #logger.info('results:%s', stdout.readlines())
                data['status'] = 'ok'
                data['cmd'][cmd]= stdout.readlines()
            return data
        except BaseException as e:
            data['status'] = 'error'
            #logger.error('connect ssh error %s:%s ',self.ip, self.port)
            #logger.error(traceback.format_exc())
            print 'connect ssh error %s:%s ' % (self.ip, self.port)
            print e
        finally:
            if ssh is not None:
                ssh.close()
            return data

    def key_connect(self, commands=[]):
        ssh = None 
        data = {}
        data['cmd']={}
        try:
            private_key_path = '/home/%s/.ssh/id_rsa' % (self.username)
            key = paramiko.RSAKey.from_private_key_file(private_key_path)            
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip, self.port, self.username, '123',key)           
            for cmd in commands:
                #logger.info('exec %s', cmd)
                print 'exec %s' % cmd
                stdin, stdout, stderr = ssh.exec_command(cmd)
                #logger.info('results:%s', stdout.readlines())
                data['status'] = 'ok'
                data['cmd'][cmd]= stdout.readlines()
            return data
        except BaseException as e:
            data['status'] = 'error'
            #logger.error('connect ssh error %s:%s ',self.ip, self.port)
            #logger.error(traceback.format_exc())
            print 'connect ssh error %s:%s ' % (self.ip, self.port)
            print e
        finally:
            if ssh is not None:
                ssh.close()
            return data

