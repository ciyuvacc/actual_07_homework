from . import app 
from flask import request,render_template,redirect,session

@app.route('/idc',methods=['GET','POST'])
def idc():
        if request.method != 'GET':
                if 'username' in session:
                        username = session.get('username')
                        return render_template('idc.html',username)
                else:
                        return redirect('/login')
        else:
                sql = "select  * from idc";
                tmp = db._execute(sql)
                cur =tmp['cur']
                str = ""
                for c in cur.fetchall():
                    print c
                    s = '<option value="%s">%s</option>' % (c[0],c[0])   #get data and get id for update,delete 
                    str = str+s
                return str
