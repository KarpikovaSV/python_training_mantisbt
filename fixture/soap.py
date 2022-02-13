from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.soap_url = app.base_url + "/api/soap/mantisconnect.php?wsdl"

    def can_login(self, username, password):
        client = Client(self.soap_url)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def projects_get(self):
        username = self.app.config['webadmin']['username']
        password = self.app.config['webadmin']['password']
        client = Client(self.soap_url)
        try:
            response = client.service.mc_projects_get_user_accessible(username, password)
            result = []
            for project in response:
                name = project.name
                result.append(Project(name=name))
            return list(result)
        except WebFault:
            return False


