from . import app 
import json
import time
from module import login_required,User,Server,Monitor,SshConnect
from flask import request,render_template,redirect,session,url_for

@app.route('/monitors',methods=["POST"])
def monitor():
    mtime = request.form.get('mtime','')
    cpu = request.form.get('cpu','')
    mem = request.form.get('mem','')
    ip = request.form.get('ip','')
    mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(mtime)))
    print mtime
    data = Monitor(ip,mtime,cpu,mem).save()
    return json.dumps({'code':data})

@app.route('/monitors/<pk>/', methods=["GET"])
def getmoniter(pk=None):
    _data = Monitor.getData(pk)    
    return json.dumps({'code' : 200, 'data': _data})

@app.route('/action/', methods=["POST"])
def action():
    ip = request.form.get('ip','')
    sshconnect = request.form.get('sshconnect','pass')
    sshname = request.form.get('sshname','')
    sshpass = request.form.get('sshpass','')
    actionarea = request.form.get('actionarea','').split('\n')
    print sshpass
    port = 22
    SSh_conn = SshConnect(ip,sshname,port)
    if sshconnect == 'pass':    
        data = SSh_conn.pass_connect(sshpass, actionarea)
    elif sshconnect == 'key':
        data = SSh_conn.key_connect(actionarea)
    print data
    return json.dumps(data)
