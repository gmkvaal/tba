from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Health(Resource):
    def get(self):
        return 'pong'


api.add_resource(Health, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')