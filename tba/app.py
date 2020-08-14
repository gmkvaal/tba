from flask import Flask
from flask_restful import Resource, Api, reqparse
from user import get_user, register_user, users

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("user_name", type=str, required=True, location="json")


class Health(Resource):
    def get(self):
        return 'pong'


class User(Resource):

    def post(self):
        args = parser.parse_args()
        user_name = args["user_name"]
        user_id = register_user(user_name=user_name)
        return {"user_id": user_id}

    def get(self, user_id: int):

        app.logger.info(users)

        try:
            user = get_user(user_id=user_id)
            return {"user_name": user.user_name}
        except KeyError:
            return {"Error": f"No user with id {user_id}"}, 404


api.add_resource(Health, "/")
api.add_resource(User, "/user", "/user/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")