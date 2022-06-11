from flask_jwt_extended import create_access_token, set_access_cookies, create_refresh_token, set_refresh_cookies, \
    unset_jwt_cookies, jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import g, request, jsonify, abort
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from marshmallow import Schema, fields

from dba import Engines, OrgUser, Organization, CaseGroupModel


class Cases(Resource):

    def __init__(self):
        self.engines = Engines()

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        org_id = current_user.get("org_id")
        role = current_user.get("user_role")

        read = self.engines.get_read()
        session = Session(read, future=True)
        statement = select(CaseGroupModel).where(CaseGroupModel.org_id == org_id).order_by(CaseGroupModel.group_name)
        with session:
            try:
                result = session.execute(statement)
                print(result)
                result = result.scalars().all()
                groups = []
                for i in result:
                    d = i.__dict__
                    d.pop('_sa_instance_state')
                    groups.append(d)
                    print("GROUPS")
                    print(groups)
                return groups
            except NoResultFound:
                response = jsonify({"msg": "login failed"})
                unset_jwt_cookies(response)
                response.status_code = 401
                return response



class CaseGroupResource(Resource):

    def __init__(self):
        self.engines = Engines()

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        org_id = current_user.get("org_id")
        role = current_user.get("user_role")

        read = self.engines.get_read()
        session = Session(read, future=True)
        statement = select(CaseGroupModel).where(CaseGroupModel.org_id == org_id).order_by(CaseGroupModel.group_name)
        with session:
            try:
                result = session.execute(statement)
                print(result)
                result = result.scalars().all()
                groups = []
                for i in result:
                    d = i.__dict__
                    d.pop('_sa_instance_state')
                    groups.append(d)
                    print("GROUPS")
                    print(groups)
                return jsonify(groups)
            except NoResultFound:
                response = jsonify({"msg": "login failed"})
                unset_jwt_cookies(response)
                response.status_code = 401
                return response


class Login(Resource):

    def __init__(self):
        self.engines = Engines()

    def post(self):
        print('LOGIN PARSE')
        print(request.json)
        email = request.json.get('username')
        password = request.json.get('password')
        read = self.engines.get_read()
        session = Session(read, future=True)
        statement = select(OrgUser).where(OrgUser.user_mail == email, OrgUser.password == password)
        with session:
            try:
                result = session.execute(statement)
                print(result)
                user = result.scalar_one()
                print("HERE")
                print(user.user_mail)
                print(user.password)

            except NoResultFound:
                response = jsonify({"msg": "login failed"})
                unset_jwt_cookies(response)
                response.status_code = 401
                return response
        jwt_info = {
            "user_id": user.id,
            "user_name": user.user_name,
            "user_mail": user.user_mail,
            "user_role": user.role,
            "status": user.status,
            "org_id": user.org_id
        }
        access_token = create_access_token(identity=jwt_info)
        refresh_token = create_refresh_token(identity=jwt_info)
        resp = jsonify({'login': True, 'data': jwt_info})
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)
        resp.status_code = 200
        return resp


class OrganizationSchema(Schema):
    organization = fields.Str(required=True)


organization_schema = OrganizationSchema()


class OrgUserResource(Resource):

    def __init__(self):
        self.engines = Engines()

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        print('OrgUserResource PARSE')
        print(request.json)
        print(current_user)
        org_id = current_user.get("org_id")
        role = current_user.get("user_role")
        if role != 0:
            return abort(400, str("Permission denied!"))
        read = self.engines.get_read()
        session = Session(read, future=True)
        statement = select(Organization).where(Organization.id == org_id)

        user = OrgUser(user_mail=request.json.get("user_mail"), user_name=request.json.get("user_name"), password=request.json.get("password"), role=request.json.get("role"), org_id=org_id)

        with session:
            # try:
            result = session.execute(statement)
            org = result.scalar_one()
            org.users.append(user)
            session.commit()
            # except:
            #     abort(409, description="A user with that username already exists.")
        resp = jsonify({"message":"Create Success"})
        resp.status_code = 200
        return resp

    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        print('OrgUserResource PARSE')
        print(request.json)
        print(current_user)
        org_id = current_user.get("org_id")
        role = current_user.get("user_role")
        if role != 0:
            return abort(400, str("Permission denied!"))
        read = self.engines.get_read()
        session = Session(read, future=True)
        user_id = request.json.get("id")
        password = request.json.get("password")
        passwordConfirm = request.json.get("passwordConfirm")
        if password != passwordConfirm:
            abort(409, description="Update Failed")
        role = request.json.get("role")
        statement = select(OrgUser).where(OrgUser.id == user_id)


        with session:
            try:
                result = session.execute(statement)
                user = result.scalar_one()
                if password:
                    user.password = password
                user.role = role
                session.commit()
            except:
                abort(409, description="Update Failed")
        resp = jsonify({"message": "Create Success"})
        resp.status_code = 200
        return resp



    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        print(current_user)
        org_id = current_user.get("org_id")
        read = self.engines.get_read()
        session = Session(read, future=True)
        statement = select(OrgUser).where(OrgUser.org_id == org_id).order_by(OrgUser.user_name)
        user_list = []
        with session:
            try:
                result = session.execute(statement).scalars().all()
                # users = result.scalar()
                for i in result:
                    print("----8")
                    print(i.__dict__)
                    d = i.__dict__
                    d.pop('_sa_instance_state')
                    d.pop('create_date')
                    d.pop('last_login_date')
                    user_list.append(d)

            except:
                pass
        return user_list


    @jwt_required()
    def get_example(self, ):
        errors = organization_schema.validate(request.args)
        if errors:
            abort(400, str(errors))