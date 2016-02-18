from . import app 
import json
from flask import request,render_template,redirect,make_response,session


@app.route('/hostmanger',methods=['POST','GET'])
def showlist():
    if request.method == 'POST':
        change = request.form.get('change')
        host =request.form.get('host')
        if "add" == change:
            ip =request.form.get('ip')
            mem =request.form.get('mem')
            end_date =request.form.get('end_date')
            sql = 'select *  from server where host = "%s"'%(host)
            tmp = app.config['cursor']._execute(sql)
            cur=tmp['cur'].fetchall()
            print cur
            if cur != ():
                return 'host already exists'
            else:
                sql = 'insert into server (host,ip,memery,end_date) values ("%s","%s","%s","%s")'%(host,ip,mem,end_date)
                tmp = app.config['cursor']._execute(sql)
                cur=tmp['cur'].fetchall()
                return tmp['msg']
        elif "update" == change:
            ip =request.form.get('ip')
            id =request.form.get('id')
            mem =request.form.get('mem')
            end_date =request.form.get('end_date')
            sql  = 'update server set host="%s",ip="%s",memery="%s",end_date="%s" where id=%s'%(host,ip,mem,end_date,id)
            tmp = app.config['cursor']._execute(sql)
            cur=tmp['cur'].fetchall()
            return tmp['msg']
        elif "delete" == change:
            id =request.form.get('id')
            sql  = 'delete from  server where host="%s" and id=%s'%(host,id)
            tmp = app.config['cursor']._execute(sql)
            cur=tmp['cur'].fetchall()
            return tmp['msg']
    page = int(request.args.get('page',1))
    num = 5
    print page
    print '000000000000'
    sql = 'select count(*) from server'
    res = app.config['cursor']._execute(sql)
    cur=res['cur'].fetchall()
    total = cur[0][0]
    if total % num ==0:
        pages = total/num
    else:
        pages =total /num +1
    if 1 < page < pages:
        nextpage =page +1
        lastpage =page - 1
    elif page >=  pages:
        lastpage = page - 1
        nextpage =pages
        page = pages
    else:
        page = 1
        lastpage = 1
        nextpage = page +1
    repage = [lastpage, nextpage, pages]
    start_position = (page - 1 ) * num
    sql = "SELECT * FROM `server` limit %s,%s" %(start_position,num)
    print sql
    tmp = app.config['cursor']._execute(sql)
    dblist = tmp['cur'].fetchall()
    data_list ={}
    data_list['repage']=repage
    data_list['data']=dblist
    print data_list
    return json.dumps(data_list)
