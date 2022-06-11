from flask_restful import Api

from resources.case_group_resource import Labels, Sections, CasesbyGroup
from resources.roles_resource import Roles
from restful_handler import Login, OrgUserResource, CaseGroupResource, Cases


def register_restful_api(flask_app):
    api = Api(flask_app)
    api.add_resource(CasesbyGroup, "/v1/cases")  # mock
    api.add_resource(Login, "/v1/auth/login")
    api.add_resource(OrgUserResource, "/v1/users")
    api.add_resource(Roles, "/roles")
    api.add_resource(CaseGroupResource, "/v1/casegroups")

    api.add_resource(Labels, "/labels")  # mock
    api.add_resource(Sections, "/sections")  # mock
