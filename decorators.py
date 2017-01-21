from models import User
def token_required(view):
    def inner(self):
        args = self.parser.parse_args()
        token = args['token']
        user = User.query.filter_by(token=token).first()
        if user:
            return view(self)
        return {"Error" : "Invalid Token"}, 403
    return inner


