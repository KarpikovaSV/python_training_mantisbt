from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.25.2/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def projects_get(self, username, password):
        client = Client("http://localhost/mantisbt-2.25.2/api/soap/mantisconnect.php?wsdl")
        try:
            response = client.service.mc_projects_get_user_accessible(username, password)
            result = []
            for project in response:
                name = project.name
                result.append(Project(name=name))
            return list(result)
        except WebFault:
            return False


