#!../venv/bin/python
import os,sys
from flask import Flask
from flask.ext.login import LoginManager
#from flask.ext.bootstrap import Bootstrap
#from config import load_config
from flask.ext.mongoengine import MongoEngine

db=MongoEngine()
#from models import db

# convert python's encoding to utf8
reload(sys)
sys.setdefaultencoding('utf8')

login_manager = LoginManager()

def create_app():
    app=Flask(__name__)
    Bootstrap(app)
    app.config.from_object('config')
    login_manager.init_app(app)
    db.init_app(app)
    register_routes(app)

    # before every request
    @app.before_request
    def before_request():
        pass
        #g.user = get_current_user()
        
    return app


def register_routes(app):
    from .controllers import site
    #account, admin,user

    app.register_blueprint(site.bp, url_prefix='')
    #app.register_blueprint(account.bp, url_prefix='/account')
    #app.register_blueprint(admin.bp, url_prefix='/admin')
    #app.register_blueprint(user.bp, url_prefix='/user')
