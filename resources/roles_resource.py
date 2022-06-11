from flask import jsonify
from flask_restful import Resource



class Roles(Resource):

    def get(self):
        data = [
            {
                "role_name": "Admin",
                "role_value": 0,
            },
            {
                "role_name": "Manager",
                "role_value": 1,
            },
            {
                "role_name": "Designer",
                "role_value": 2,
            },
            {
                "role_name": "Tester",
                "role_value": 3,
            },
            {
                "role_name": "Viewer",
                "role_value": 4,
            },
        ]
        return jsonify(data)

    def put(self):
        return  {}