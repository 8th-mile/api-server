from user import *
from event import *
app = Flask(__name__)

if __name__ == '__main__':
    db.create_all()
    api = Api(app, catch_all_404s=True, errors=CUSTOM_ERRORS)
    api.add_resource(UserSignup, '/user/signup')
    api.add_resource(EventRegister, '/event')
    app.run(debug=True)


