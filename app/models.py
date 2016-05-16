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
    last_seen = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    league_tag=db.relationship('League', backref='users')

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


class Athlete(db.Model):
    __tablename__='athletes'
    id=db.Column(db.Integer,primary_key=True)
    athlete_name=db.Column(db.String(30))
    weight=db.Column(db.Integer)
    age=db.Column(db.Integer)
    nationality=db.Column(db.String(20))
    is_selected=db.Column(db.Boolean)
    team_id=db.Column(db.Integer,db.ForeignKey('team.id'),unique=True)


class Draft(db.Model):
    __tablename__='draft'
    id=db.Column(db.Integer,primary_key=True)
    date=db.Column(db.DateTime)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),unique=True)
    athlete_id=db.Column(db.Integer,db.ForeignKey('athletes.id'),unique=True)



class Draft_Room(db.Model):
    __tablename__='draft_room'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30))
    chat=db.Column(db.String(1000))
    date=db.Column(db.DateTime)
    draft_id=db.Column(db.Integer,db.ForeignKey('draft.id'),unique=True)


class Payment(db.Model):
    __tablename__='payment'
    id=db.Column(db.Integer,primary_key=True)
    card_type=db.Column(db.String(20))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),unique=True)

class Prize(db.Model):
    __tablename__='prize'
    id=db.Column(db.Integer,primary_key=True)
    throphy_type=db.Column(db.String(20))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),unique=True)


class League(db.Model):
    __tablename__='league'
    id=db.Column(db.Integer,primary_key=True, unique=True)
    league_name=db.Column(db.String(20), unique=True, nullable=False)
    number_of_team=db.Column(db.Integer, nullable=False)
    league_type=db.Column(db.String(30), nullable=False)
    game_type=db.Column(db.String(30),nullable=False)
    match_type=db.Column(db.String(30), nullable=False)
    champion=db.Column(db.String(30), nullable=False)
    create_date=db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    url=db.Column(db.String(500), nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),unique=True)

    def __init__(self, league_name, number_of_team, league_type, game_type, match_type, champion, url, user_id):
        self.league_name=league_name
        self.number_of_team=number_of_team
        self.league_type=league_type
        self.game_type=game_type
        self.match_type=match_type
        self.champion=champion
        self.url=url
        self.user_id=user_id

class Trades(db.Model):
    __tablename__='trades'
    id=db.Column(db.Integer,primary_key=True)
    trade_date=db.Column(db.DateTime)
    team_id=db.Column(db.Integer,db.ForeignKey('team.id'),unique=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),unique=True)
    athletes_id=db.Column(db.Integer,db.ForeignKey('athletes.id'),unique=True)
    season_id=db.Column(db.Integer,db.ForeignKey('season.id'),unique=True)

class Season(db.Model):
    __tablename__='season'
    id=db.Column(db.Integer,primary_key=True)
    draft_date=db.Column(db.DateTime)
    first_game_date=db.Column(db.DateTime)
    league_id=db.Column(db.Integer,db.ForeignKey('league.id'),unique=True)

class Fixture(db.Model):
    __tablename__='fixtue'
    id=db.Column(db.Integer,primary_key=True)
    match_date=db.Column(db.DateTime)
    upcoming_date=db.Column(db.DateTime)
    Result=db.Column(db.Integer)
    season_id=db.Column(db.Integer,db.ForeignKey('season.id'),unique=True)

class Champion(db.Model):
    __tablename__='champion'
    id=db.Column(db.Integer,primary_key=True)
    rank=db.Column(db.Integer)
    league_id=db.Column(db.Integer,db.ForeignKey('league.id'),unique=True)
