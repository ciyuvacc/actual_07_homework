#encoding: utf-8

from flask import Flask

from app1 import views as app1view
from app2 import views as app2view
    
app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(app1view.bp)
    app.register_blueprint(app2view.bp)
    app.run(host='0.0.0.0', port=9005, debug=True)
