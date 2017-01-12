from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

from models import User, db
from errors import *

class UserSignup(Resource):
    def get(self):
        return {"Success" : "true"}

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')
        self.parser.add_argument('phone')
        self.parser.add_argument('email')

    def post(self):
        # Extract data from URL
        args = self.parser.parse_args()
        name = args['name']
        phone = args['phone']
        email = args['email']

        # Validate data
        if not name:
            raise NameEmptyError()
        if not email:
            raise EmailEmptyError()
        if not phone:
            raise InvalidPhoneNumberError()

        #Insert into database
        try:
            user_db_object = User(name, phone, email)
            db.session.add(user_db_object)
            db.session.commit()
        except Exception as exception:
            print exception
            raise DBInsertError()

        # Check if user insertion is successfull in db
        try:
            inserted_user = User.query.filter_by(phone=phone).first()

            return {"success":"true", "otp" : int(inserted_user.otp)}

        except:
            raise DBQueryError()


class UserVerify(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('phone')
        self.parser.add_argument('otp')

    def post(self):
        args = self.parser.parse_args()
        phone = args['phone']
        otp = args['otp']
        user = User.query.filter_by(phone=phone, otp=otp).first()
        if user:
            return User
        return {"Success": "false", "message" : "Phone and Otp don't match"}


def authenticate(phone, otp):
    args = self.parser.parse_args()
    phone = args['phone']
    otp = args['otp']
    user = User.query.filter_by(phone=phone, otp=otp).first()
    if user:
        return User
    return {"Success": "false", "message" : "Phone and Otp don't match"}

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)

jwt = JWT(app, authenticate, identity)
@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

