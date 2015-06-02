import datetime
from flask import url_for
from app import db


class comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="Comment", required=True)
    author = db.StringField(verbose_name="Name", max_length=255, required=True)

class good(db.EmbeddedDocument):
    name=db.StringField(max_length=255,required=True)
    image=db.StringField(required=True)
    charge=db.FloatField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    is_active=db.BooleanField(required=True,default=True)
    sold_number=db.IntField(required=True,default=0)
    thumbsup=db.IntField(default=0,required=True)
    thumbsdown=db.IntField(default=0,required=True)
    comments=db.ListField(db.EmbeddedDocumentField('comment'))


class shop(db.Document):
    name=db.StringField(max_length=255,required=True)
    logo=db.StringField(max_length=255,required=True)
    address=db.StringField(max_length=255,required=True)
    descript=db.StringField(required=True)
    information=db.StringField(required=True)
    contact=db.StringField(required=True)
    number_of_goods=db.IntField(required=True)
    threadshold=db.IntField(required=True)
    deliver_time=db.ListField(db.StringField(),required=True)
    owner=db.StringField(required=True)
    goods=db.ListField(db.EmbeddedDocumentField('good'),default=[])


class test(db.Document):
    name=db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)

class User(db.Document):
    nickname = db.StringField(max_length=255,unique = True,required=True)
    password=db.StringField(required=True)
    email = db.EmailField(unique = True)
    login_times=db.IntField(required=True,default=0)
    last_login=db.DateTimeField(required=True,default=datetime.datetime.now)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

# class shopcarts(db.Document):
#     buyer
#     shop
#     items(
#         goodsid
#         goodsname
#         is_commented
#         is_add_commented
#         is_send_back
#     )
#     sum_of_charge
#     deliver_time 
#     state(buy,prepare,send,incharge,finished)

# class user
#     name
#     address
#     contact
#     logo
#     history_payment
#     in_proceed_payment
#     goodstatement
#     is_seller
#     imbed_carts