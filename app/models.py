from datetime import datetime
import hashlib
from markdown import markdown
import bleach
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import request, current_app
from flask.ext.login import UserMixin
from . import db
from hashlib import md5


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64),
                      nullable=False, unique=True, index=True)
    username = db.Column(db.String(64),
                         nullable=False, unique=True, index=True)
    is_admin = db.Column(db.Boolean)
    password_hash = db.Column(db.String(128))
    user_info=db.relationship('PersonalInfo' ,uselist=False,backref='users',cascade="save-update, merge, delete")
    last_seen = db.Column(db.DateTime)

    def __init__(self, email, username, is_admin,password):
        self.email=email
        self.username=username
        self.is_admin=is_admin
        self.password_hash=generate_password_hash(password)

    def __repr__(self):
        return "<User(email='%s', username='%s')>" %(self.email, self.username)
    @property
    def password(self):
        raise AttributeError('password is not a readable')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)


class PersonalInfo(db.Model):
    __tablename__= 'user_info'
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(30), default="None")
    last_name=db.Column(db.String(30), default="None")
    country=db.Column(db.String(30), default="None")
    city=db.Column(db.String(30), default="None")
    phonenumber=db.Column(db.Integer,default=20)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)

    def __init__(self, first_name,last_name, country,city,phonenumber):
        self.first_name=first_name
        self.last_name=last_name
        self.country=country
        self.city=city
        self.phonenumber=phonenumber


    def __repr__(self):
        return "<User Info(FirstName='%s', LastName='%s')>" %(self.first_name, self.last_name)

class Team (db.Model):
    __tablename__ ='team'
    id = db.Column(db.Integer, primary_key=True)
    team_name= db.Column(db.String(20))
    points=db.Column(db.Integer)
    knockout=db.Column(db.Integer)
    submission=db.Column(db.Integer)
    decision_score = db.Column(db.Integer)
    score=db.Column(db.Integer)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
