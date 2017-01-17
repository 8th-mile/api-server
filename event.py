from flask import Flask, Response, jsonify
from flask_restful import Resource, Api, reqparse
from errors import *
from models import Event, db, User

import datetime
import pyqrcode
from collections import OrderedDict
from pprint import pformat

QRCODE_PATH = "qrcodes/"

class Eventadd(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('type')
        self.parser.add_argument('name')
        self.parser.add_argument('date')
        self.parser.add_argument('venue')
        self.parser.add_argument('price')

    def get(self):
        events = Event.query.all()
        print type(events)
        event_list = []
        for event in events:
            event_list.append(
                {'id' : event.id,
                 'name': event.name,
                 'date': event.datetime,
                 'venue': event.venue,
                 'type': event.type,
                 'price': event.price
                 }                
                )
        return jsonify(results = event_list)

    def post(self):
        args = self.parser.parse_args()
        type = args['type']
        name = args['name']
        event_date = args['date']
        event_date = event_date.split('/')
        # TODO : Check if date format is right => Are there 3 items in list?
        day, month, year = (int(d) for d in event_date)
        db_date = datetime.date(year, month, day)
        venue = args['venue']
        price = args['price']
        try:
            event = Event(type, name, db_date, venue, price)
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

        event = Event.query.get(event_id)
        user = User.query.get(user_id)
        try:
            user.events.append(event)
            db.session.add(user)
            db.session.commit()

            # Generate QR code
            qr_payload = OrderedDict()
            qr_payload["User ID"] = str(user.id)
            qr_payload["Event ID"] = str(event.id)
            qr_payload["Date"] = str(event.datetime)
            qr_payload["Venue"] = event.venue
            qr_payload["Price"] = str(event.price)

            code = pyqrcode.create(str(qr_payload))
            qrcode_file_name = event.name + "--" + str(user.id) + ".svg"
            qr_link = QRCODE_PATH + qrcode_file_name
            code.svg(qr_link, scale=8)
            return {"success" : "true",
                    "link": qr_link}
        except Exception as exception:
            print exception
            return DBInsertError()
