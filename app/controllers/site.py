# coding: utf-8
from flask import render_template, Blueprint, request, get_template_attribute,jsonify
from app import login_manager
from flask.ext.login import current_user, login_required, login_user, logout_user
from app.models import *
import datetime

@login_manager.user_loader
def load_user(userid):
    return User.objects(id=userid).first()

bp = Blueprint('site', __name__)

@bp.route('/')
def index():
    """首页"""
    return render_template('site/index.html')
    #return render_template('site/index.html', works=works, work_images=work_images,
     #                      work_reviews=work_reviews, authors=authors, dynasties=dynasties)

@bp.route('/about')
def about():
    """about"""
    return jsonify({'info':'This is the page about the site!店铺好评数'})#return render_template('site/about.html')

@bp.route('/user')
@login_required
def user():
    """userlist"""
    return jsonify(user=unicode(current_user))

@bp.route('/loginid/<id>',methods=['GET','POST'])
def loginid(id):
    """userlogin"""
    a=User.objects(id=id)
    if a.first() and a.first().password=='password':
            # 儲存 session
            login_user(a.first())
            a.update_one(inc__login_times=1)
            a.update_one(set__last_login=datetime.datetime.now)
            return jsonify({'login-ok':a})
    return jsonify({'login-failed':'failed'})

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({'logout':'ok'})

@bp.route('/shop')
def shoplist():
    """shoplist"""
    shops=shop.objects().all()
    return jsonify(shops=shops)

@bp.route('/ajax')
def ajax():
    """ajax"""
    return render_template('site/ajax.html')