from . import app 
import json
from module import login_required,User,Server
from flask import request,render_template,redirect,session,url_for

@app.route('/index')
@login_required
def index():
    
    return render_template("index.html",username=session['username'])

@app.route('/users',methods=['POST','GET'])
@login_required
def getdata():
    if request.method == 'POST': 
        change = request.form.get('change')
        print request.form
        user = User(request.form)
        if "add" == change:
            status = user._sign()
            return status
        if "update" == change:
            print 'now is change'
            status = user._changeuser()
            return status
        if "delete" == change:
            status = user._deluser()
            return status

    query = request.args.get('query','')
    nowpage = int(request.args.get('page',1))
    pagesize = 10
    data_list = User._page(nowpage,pagesize,query)

    return render_template("users.html",data_list=data_list,username=session['username'])

@app.route('/assets',methods=['POST','GET'])
@login_required
def assets():
    page = int(request.args.get('page',1))
    return render_template("asset.html",page=page,username=session['username'])

@app.route('/getserverdata',methods=['POST','GET'])
@login_required
def serverdata():
    if request.method == 'POST': 
        change = request.form.get('change')
        print request.form
        server = Server(request.form)
        if "add" == change:
            status = server._select()
            return status
        if "update" == change:
            print 'now is change'
            status = user._changeuser()
            return status
        if "delete" == change:
            status = user._deluser()
            return status

    query = request.args.get('query','') 
    nowpage = int(request.args.get('page',1))
    pagesize = 5
    data_list = Server._select(nowpage,pagesize,query)
    print data_list
    return json.dumps(data_list)
