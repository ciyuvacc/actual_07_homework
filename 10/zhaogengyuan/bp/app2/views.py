#encoding: utf-8

from flask import Blueprint
from flask import render_template

bp = Blueprint('app2', __name__, url_prefix='/app2', template_folder='templates', static_folder='static')

@bp.route('/') # /app2/
def index():
    return render_template('index.html')
