import json
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app) #Die Flask API


data ={}
class SimpleClass(Resource):
    def get(self):
        with open('mydata.json') as f:
            events = json.load(f)
            a = events["playerstats"]
        return a



api.add_resource(SimpleClass, '/')


if __name__ == '__main__':
    app.run(debug=True) #debug=True lädt nach den Änderungen neu

