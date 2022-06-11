from flask import jsonify
from flask_restful import Resource


class Users(Resource):

    def get(self):
        data = [
            {
                "name": "fabian1",
                "mail": "fabianlin@keenlity.com",
                "role": "admin",
                "last_login": "2022/02/22 12:16:15",
                "status": "Active"
            },
            {
                "name": "vicky",
                "mail": "vicky@keenlity.com",
                "role": "manager",
                "last_login": "2022/02/22 12:16:15",
                "status": "Active"
            },
        ]
        return jsonify(data)

    def put(self):
        return  {}