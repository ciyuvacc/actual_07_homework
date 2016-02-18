from . import app
import json
from flask import request,render_template,redirect,make_response,session
from module import count_log 


@app.route('/log')
def log():
    infile='../www_access_20140823.log'
    tmp_dic = count_log(infile)
    for i,v in tmp_dic.items():
        sql = 'insert into log (ip,url,status,value) values ("%s","%s","%s","%s")'% (i[0],i[1],i[2],v)
        tmp = app.config['cursor']._execute(sql)
        cur=tmp['cur'].fetchall()
    return render_template('showlog.html')

@app.route('/showlog')
def showlog():
    node = int(request.args.get('count')) 
    print 'node %s' % node
    arr_list=[]
    len_list = 0 
    sql = 'select status,url,ip,value from log order by value desc limit %d ' % (node)
    tmp = app.config['cursor']._execute(sql)
    arr_list = tmp['cur'].fetchall()
    sql = 'select count(*) from log'
    tmp1 = app.config['cursor']._execute(sql)
    len_list = tmp1['cur'].fetchall()
    data_dict ={} 
    data_dict['len']=len_list
    data_dict['data']=arr_list
    return json.dumps(data_dict)
