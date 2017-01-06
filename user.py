from flask import Flask
from flask_restful import Resource, Api, reqparse

from models import User, db
from errors import *



class UserSignup(Resource):
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
        if len(name) == 0:
            raise NameEmptyError()
        if len(email) == 0:
            raise EmailEmptyError()
        if len(phone) != 10:
            raise InvalidPhoneNumberError()

        #Insert into database
        try:
            user_db_object = User(name, phone, email)
            db.session.add(user_db_object)
            db.session.commit()
        except:
            raise DBInsertError()

        # Check if user insertion is successfull in db
        try:
            inserted_user = User.query.filter_by(phone=phone).first()
            if inserted_user is None:
                return {"success": "false"}, 400
            else:
                return {"success":"true", "name" : inserted_user.username}
        except:
            raise DBQueryError()


if __name__ == '__main__':
    db.create_all()
    app = Flask(__name__)
    api = Api(app, catch_all_404s=True, errors=CUSTOM_ERRORS)
    api.add_resource(UserSignup, '/user/signup')
    app.run(debug=True)
