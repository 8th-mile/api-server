from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import requests

from models import User, Event, db
from errors import *
from decorators import token_required

class UserSignup(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('idtoken')
        #self.parser.add_argument('phone')
        self.parser.add_argument('email')

    def post(self):
        # Extract data from URL
        args = self.parser.parse_args()
        idtoken = args['idtoken']
        email = args['email']

        # Validate data
        if not idtoken:
            raise NameEmptyError()
        if not email:
            raise EmailEmptyError()
        
        user = User.query.filter_by(email=email).first()
        if not user:

        #Insert into database
            url = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token={}'.format(idtoken)
            try:
                data = requests.get(url).json()
                user = User(username=data['name'], email=data['email'],
                        photo=data['picture'], kid=data['kid'])
                db.session.add(user)
                db.session.commit()
                return {"success" : "true", "id" : user.id, "name": user.username, 'token' : user.token}
            except Exception as exception:
                print exception
                raise DBInsertError()

        return {"success" : "true", "id" : user.id, "name" : user.username, 'token' : user.token}


class UserWish(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('user_id')
        self.parser.add_argument('event_id')
        self.parser.add_argument('token', location='headers')
 
    
    @token_required
    def get(self):
        args = self.parser.parse_args()
        user_id = args['user_id']
        user = User.query.filter(user_id).first_or_404()

        wished_events = user.wishlist_events
        event_list = []
        for event in wished_events:
            event_list.append(
                {'name': event.name,
                 'date': event.datetime,
                 'type': event.type,
                 'price': event.price
                 }
            )
        return jsonify(results=event_list)

    @token_required
    def post(self):
        args = self.parser.parse_args()
        user_id = args['user_id']
        event_id = args['event_id']

        event = Event.query.get(event_id) # TODO : Try get(primary key)method
        user = User.query.get(user_id)

        try:
            user.wishlist_events.append(event)
            db.session.add(user)
            db.session.commit()
            return {"success": "true"}
        except Exception as exception:
            print exception
            return DBInsertError()

class UserInfo(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('user_id')
        self.parser.add_argument('token', location='headers')


    @token_required
    def get(self):
        args = self.parser.parse_args()
        user_id = args['user_id']
        user = User.query.get(user_id)

        return {
            "id": user.id,
            "name": user.username,
            "registered events": [event.id for event in user.events],
            "events in wishlist": [event.id for event in user.wishlist_events]
}
