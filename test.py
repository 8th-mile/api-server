import requests
from flask_restful import Resource, Api, reqparse
from flask import Flask
app = Flask(__name__)

class test(Resource):
    def get(self):
        parser = reqparse.RequestParser() 
        parser.add_argument('arg')
        args = parser.parse_args()
        print args
        return {"Success" : "True"}

@app.route('/some-url')
def get_data():
    url = 'https://www.{}.co.in/'.format('google')
    print url
    data = requests.get(url).content 
    print data
    return requests.get(url).content 

if __name__ == '__main__':
    api = Api(app, catch_all_404s=True)

    api.add_resource(test, '/test')


    app.run(debug=True)

