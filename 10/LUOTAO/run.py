#!/usr/bin/env python

from app import app
import dbconf
from mydb import DB

if __name__=='__main__':
     app.config['cursor']=DB(dbconf.DB_HOST,dbconf.DB_USER,dbconf.DB_PASSWD,dbconf.DB_DATABASE,dbconf.DB_PORT,dbconf.DB_CHARSET)
     app.secret_key='daki1931&8187151%W&1DK1JF19384'
     app.run(debug=True,host='0.0.0.0',port=9090)

