from . import app 
import json
import time
from module import login_required,User,Server,Monitor
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

