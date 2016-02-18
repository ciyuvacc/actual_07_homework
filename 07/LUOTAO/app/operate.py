from . import app
import json
from flask import request,render_template,redirect,make_response,session
from module import init_func1


@app.route('/jisuanqi')
def jisuanqi():
    return render_template('operate.html')

@app.route('/operate')
def operate():
    mystr = request.args.get('mycount')
    mystr= mystr.encode("utf-8")
    count = init_func1(mystr)
    return str(count)
