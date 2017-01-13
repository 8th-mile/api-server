from user import *
from event import *
from sponsor import *
app = Flask(__name__)

if __name__ == '__main__':
    db.create_all()
    api = Api(app, catch_all_404s=True, errors=CUSTOM_ERRORS)

    api.add_resource(UserInfo, '/user')
    api.add_resource(UserSignup, '/user/signup')
    api.add_resource(UserVerify, '/user/verify')
    api.add_resource(UserWish, '/user/wish')
    api.add_resource(Eventadd, '/event')
    api.add_resource(EventRegister, '/event/register')
    api.add_resource(AddSponsor, '/sponsor')

    app.run(debug=True)


