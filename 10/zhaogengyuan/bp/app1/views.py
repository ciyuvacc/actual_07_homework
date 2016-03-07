#encoding: utf-8

from flask import Blueprint
from flask import render_template

bp = Blueprint('app1', __name__, url_prefix='/app1', template_folder='templates', static_folder='static')

@bp.route('/') # /app1/
def index():
    return render_template('app1/index.html')