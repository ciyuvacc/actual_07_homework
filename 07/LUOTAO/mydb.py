import MySQLdb as mysql

class DB():
    def __init__(self,host,user,passwd,db,port,charset):
        self.host = host 
        self.user = user
        self.passwd = passwd
        self.db = db  
        self.port = port
        self.charset = charset
        self.conn = None
        self._connect()
    def _connect(self):
        self.conn = mysql.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=self.port,charset=self.charset)
        self.conn.autocommit(True)
    def _execute(self,sql):
        msg= 'ok'
        try:
            print 'connect db'
            cur = self.conn.cursor()
            cur.execute(sql)
        except Exception,e:
            print e
            print 'reconnect db123'
            self._connect()
            cur =self.conn.cursor()
            try:
                cur.execute(sql)
            except Exception,e:
                print e
                msg = 'error in sql'
            self.conn.close()
            cur.close()
        return {'cur':cur,'msg':msg}
