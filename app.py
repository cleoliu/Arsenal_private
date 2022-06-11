import datetime
import json

from flask import Flask, request, jsonify, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, set_access_cookies, \
    get_jwt
from flask_restful import Resource, Api

from resources.case_group_resource import CaseGroups, CasesbyGroup, Labels, Sections
from resources.roles_resource import Roles
from resources.users_reources import Users
from restful import register_restful_api


app = Flask(__name__)
app.config['JWT_TOKEN_LOCATION'] = ['headers', "cookies"]
app.config['JWT_SECRET_KEY'] = 'K0E9E55N8L5I8T0Y6q7a2e7n4g0i8n0e1eristhebest'
app.config['JWT_COOKIE_SECURE'] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=1)
app.config['JWT_SESSION_COOKIE'] = True
jwt = JWTManager()
jwt.init_app(app)

register_restful_api(app)





@app.after_request
def refresh_expiring_jwts(response):
    try:
        print(":REFRES!---")
        exp_timestamp = get_jwt()["exp"]
        now = datetime.datetime.now(datetime.timezone.utc)
        target_timestamp = datetime.datetime.timestamp(now + datetime.timedelta(minutes=30))
        print(exp_timestamp, now, target_timestamp)
        if target_timestamp > exp_timestamp:
            print("REAL REFRESH")
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response


@app.route('/')
def login_page():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login11():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    print(username, password)

    # if username != 'test' or password != 'test':
    #     return jsonify({"msg": "Bad username or password"}), 401

    response = jsonify({"msg": "login successful"})
    access_token = create_access_token(identity=username)
    set_access_cookies(response, access_token, max_age=100)
    return response, 200


@app.route('/team')
@jwt_required(optional=False)
def teams():  # put application's code here
    current_user = get_jwt_identity()
    print(current_user)
    return render_template('team.html')


@app.route('/case')
@jwt_required(optional=False)
def cases():  # put application's code here
    current_user = get_jwt_identity()
    print(current_user)
    return render_template('cases.html')


@app.route('/runs')
# @jwt_required(optional=False)
def runs():  # put application's code here
    # current_user = get_jwt_identity()
    # print(current_user)
    return render_template('runs.html')


@app.route('/tests')
@jwt_required(optional=False)
def tests():  # put application's code here
    current_user = get_jwt_identity()
    print(current_user)
    return render_template('tests.html')


if __name__ == '__main__':
    app.run(debug=True)
