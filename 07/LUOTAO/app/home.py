from . import app 
import json
from flask import request,render_template,redirect,session,url_for

@app.route('/index')
def index():
    if 'username' not in session:
        return redirect(url_for('main'))
    else:
        page = int(request.args.get('page',1))
        return render_template('index.html',username=session['username'],page=page)
