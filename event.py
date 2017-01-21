from flask import Flask, Response, jsonify
from flask_restful import Resource, Api, reqparse
from errors import *
from models import Event, db, User
import datetime
from decorators import token_required

from pprint import pformat
now = datetime.datetime.utcnow()

class Eventadd(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('type')
        self.parser.add_argument('name')
        self.parser.add_argument('date')
        self.parser.add_argument('price')
        self.parser.add_argument('token', location='headers')
    @token_required
    def get(self):
        events = Event.query.all()
        event_list = []
        for event in events:
            event_list.append(
                {'id' : event.id,
                 'name': event.name,
                 'date': event.datetime,
                 'type': event.type,
                 'price': event.price
                 }                
                )
        return jsonify(results = event_list)
    
    @token_required
    def post(self):
        args = self.parser.parse_args()
        type = args['type']
        name = args['name']
        event_date = args['date']

        event_date = event_date.split('/')
        # TODO : Check if date format is right => Are there 3 items in list?
        day, month, year = (int(d) for d in event_date)
        db_date = datetime.date(year, month, day)
        print pformat(db_date)
        price = args['price']
        try:
            event = Event(type, name, db_date, price)
            db.session.add(event)
            db.session.commit()
            return {"Success" : "true"}
        except Exception as exception:
            print exception
            raise DBInsertError()

class EventRegister(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('user_id')
        self.parser.add_argument('event_id')
        self.parser.add_argument('token', location='headers')

    @token_required
    def post(self):
        args = self.parser.parse_args()
        user_id = args['user_id']
        event_id = args['event_id']

        event = Event.query.get(event_id)
        user = User.query.get(user_id)
        try:
            user.events.append(event)
            db.session.add(user)
            db.session.commit()
            return {"success" : "true"}
        except Exception as exception:
            print exception
            return DBInsertError()
