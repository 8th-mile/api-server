from flask import Flask, Response, jsonify
from flask_restful import Resource, Api, reqparse
from errors import *
from models import Event, db, User
import datetime

now = datetime.datetime.utcnow()

class Eventadd(Resource):
    def get(self):
        events = Event.query.all()
        event_list = []
        for event in events:
            event_list.append(
                {'name': event.name,
                 'date': event.datetime,
                 'type': event.type,
                 'price': event.price
                 }                
                )
        return {'events': event_list}

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('type')
        self.parser.add_argument('name')
        self.parser.add_argument('date')
        self.parser.add_argument('price')

    def post(self):
        args = self.parser.parse_args()
        type =  args['type']
        name = args['name']
        date = now
        price = args['price']
        try:
            event = Event(type, name, date, price)
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

    def post(self):
        args = self.parser.parse_args()
        user_id = args['user_id']
        event_id = args['event_id']

        event = Event.query.filter(event_id).first_or_404()
        user = User.query.filter(user_id).first_or_404()
        try:
            user.events.append(event)
            db.session.add(user)
            db.session.commit()
            return {"success" : "true"}
        except Exception as exception:
            print exception
            return DBInsertError()
