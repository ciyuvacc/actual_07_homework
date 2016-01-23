#!/bin/env python
# -*- encoding:utf-8 -*-
# arithmetic_web.py
# Author : Jacob.Yu
# CTime : 2016-01-22

from flask import Flask
from flask import request
from flask import render_template
#from flask import redirect
import arithmetic_with_priority

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world 2'

# http://10.2.1.26:81/calculate/
@app.route('/calculate/',methods=["post","get"])
def calculate():
    formula = request.form.get('formula')
    if formula is not None:
        expr_list = arithmetic_with_priority.split_expr(formula)
        show_result = arithmetic_with_priority.arithmetic_with_priority(expr_list)
        return render_template('calculation.html',show_result=show_result)
    else:
        return render_template('calculation.html',formula="1+2*3-4+5*6")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=81,debug=True)



'''
还可以，尽量跟着作业做，能做多少算多少，但是如果有问题尽量能够寻问下别的同学，继续加油
'''