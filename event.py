from flask import Flask, Response, jsonify
from flask_restful import Resource, Api, reqparse
from errors import *
from models import Event, db
import datetime

now = datetime.datetime.utcnow()

class EventRegister(Resource):
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
        except Exception as exception:
            print exception
            raise DBInsertError()
