from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse

from models import User, db

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('phone')

class UserSignup(Resource):
    def __init__(self):
        #parser = reqparse.RequestParser()
        pass
    def post(self):
        args = parser.parse_args()
        name = args['name']
        phone = args['phone']
        email = request.form['email']

        #return {"success": "true", "name": name, "phone" : phone}

        #Insert into db
        user_db_object = User(name, phone, email)
        db.session.add(user_db_object)
        db.session.commit()

        #check if user insertion is successfull in db
        inserted_user = User.query.filter_by(phone=phone).first()
        print inserted_user.username
        if inserted_user is None:
            return {"success": "false"}, 400
        else:
            return {"success":"true", "name" : inserted_user.username} # default is 200


#api.add_resource(HelloWorld, '/')
api.add_resource(UserSignup, '/user/signup')

if __name__ == '__main__':
    app.run(debug=True)
