import datetime
from app import db

class Village(db.Document):
    name=db.StringField(required=True)
    region=db.PolygonField()

class comment(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(required=True)
    author = db.StringField(max_length=255, required=True)

class good(db.Document):
    name=db.StringField(max_length=255,required=True)
    image=db.StringField(required=True)
    charge=db.FloatField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    is_active=db.BooleanField(required=True,default=True)
    sold_number=db.IntField(required=True,default=0)
    thumbsup=db.IntField(default=0,required=True)
    thumbsdown=db.IntField(default=0,required=True)
    comments=db.ListField(db.ReferenceField(comment))

    meta = {
        'indexes': [
            {
                'fields': ['created_at']
            }
        ]
    }

class user(db.Document):
    name = db.StringField(max_length=255,unique = True,required=True)
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
        return '<User %r>' % (self.name)

class shop(db.Document):
    name=db.StringField(max_length=255,required=True)
    logo=db.StringField(max_length=255,required=True)
    village=db.ReferenceField(Village)
    address=db.StringField(max_length=255,required=True)
    description=db.StringField(required=True)
    information=db.StringField(required=True,default='')
    contact=db.StringField(required=True,default='')
    number_of_goods=db.IntField(required=True,default=30)
    threadshold=db.IntField(required=True,default=20)
    deliver_time=db.ListField(db.StringField(),required=True,default=[])
    owner=db.ReferenceField(user,required=True)
    created_at=db.DateTimeField(default=datetime.datetime.now, required=True)
    goods=db.ListField(db.ReferenceField('good'))
    thumbsup=db.IntField(default=0,required=True)
    thumbsdown=db.IntField(default=0,required=True)

    meta = {
        'indexes': [
            {
                'fields': ['created_at']
            }
        ]
    }

class cartsitem(db.Document):
    good=db.ReferenceField(good)
    is_commented=db.BooleanField()
    is_add_commented=db.BooleanField()

CARTSSTATE = ('deal', 'prepare', 'send', 'incharge', 'finished')

class shopcarts(db.Document):
     buyer=db.ReferenceField(User,required=True)
     shop=db.ReferenceField(shop,required=True)
     items=db.ListField(db.ReferenceField(cartsitem))
     sum_of_charge=db.IntField()
     deliver_time=db.StringField()
     state=db.StringField(choices=CARTSSTATE)
