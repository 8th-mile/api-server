from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from models import db, Event, Sponsors
from errors import *

class AddSponsor(Resource):
    def get(self):
        sponsors = Sponsors.query.all()
        sponsor_list = []
        for sponsor in sponsors:
            sponsor_events = []
            events = sponsor.events.all()
            for event in events:
                sponsor_events.append({'event' : event.id})
            sponsor_list.append(
                {'name': sponsor.name,
                 'logo': sponsor.logo_url,
                 'event': sponsor_events
                 }                
                )
        return jsonify(results = sponsor_list)

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')
        self.parser.add_argument('logo')
        self.parser.add_argument('event_id')
 
    def post(self):
        args = self.parser.parse_args()
        name =  args['name']
        logo  = args['logo']
        event_id = args['event_id']
        try:
            sponsor = Sponsors(name, logo)
            event = Event.query.get(event_id)
            event.sponsors.append(sponsor)
            db.session.add(sponsor, event)
            db.session.commit()
            return {"Success" : "true"}
        except Exception as exception:
            print exception
            raise DBInsertError()
