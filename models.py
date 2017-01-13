from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:@localhost/mile1'

db = SQLAlchemy(app)

users = db.Table('user_event_mapping', 
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
       )
wishlist_events = db.Table('wishlist_events',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
       )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    phone = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(128), unique=True)
    otp = db.Column(db.Integer, unique=True)
    
    first_places = db.relationship('Event', backref='first_user',foreign_keys='Event.winner_id', lazy='dynamic')
    second_places = db.relationship('Event', backref='second_user',foreign_keys='Event.second_id', lazy='dynamic')
    third_places = db.relationship('Event', backref='third_user', foreign_keys='Event.third_id',lazy='dynamic')
    events = db.relationship('Event', secondary='user_event_mapping',
            #foreign_keys='Event',
            backref=db.backref('event_users', lazy='dynamic'))
    wishlist_events = db.relationship('Event', secondary=wishlist_events,
            backref=db.backref('event_keeners', lazy='dynamic'))

    def __init__(self, username, phone, email):
        self.username = username
        self.email = email
        self.phone = phone
        self.otp = random.randint(10000, 99999)

    def __repr__(self):
        return '<User %r>' %self.username

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    name = db.Column(db.String(64), unique=True)
    total_tickets = db.Column(db.Integer)
    avail_tickets = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lug = db.Column(db.Float)
    price = db.Column(db.Integer)
    datetime = db.Column(db.DateTime)
    winner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    second_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    third_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_prize = db.Column(db.Integer)
    second_prize = db.Column(db.Integer)
    third_prize = db.Column(db.Integer)

    sponsors = db.relationship('Sponsors', secondary='sponsors_event_mapping',
            backref=db.backref('events', lazy='dynamic'))
    coordinator = db.relationship('coordinator', backref='coordinator.event', lazy='dynamic')

    def __init__(self, type, name, date, price):
        self.type = type
        self.name = name
        self.datetime = date
        self.price = price
    
    def __repr__(self):
        return '<Event %r>' %self.name

class Sponsors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    logo_url = db.Column(db.String(256))

    def __init__(self, name, logo):
        self.name = name
        self.logo_url = logo

    def __repr__(self):
        return '<Sponsor %r>' %self.name
 
sponsors = db.Table('sponsors_event_mapping',
        db.Column('sponsor_id', db.Integer, db.ForeignKey('sponsors.id')),
        db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
        )

class coordinator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.Integer, db.ForeignKey('event.id'))
    username = db.Column(db.String(64))
    password = db.Column(db.String(256))
    
class publicity_team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer)
    publicity_user = db.relationship('publicity_user', backref='publicity_team_user', lazy='dynamic')

class publicity_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(256))
    publicity_team = db.Column(db.Integer, db.ForeignKey('publicity_team.id'))
    def __repr__(self):
        return '<Pub_user %r>' %self.name
