# To work on the SOAP protocol, you need the suds-jurko library
from suds import WebFault # Exception (if something is wrong with the connection)
from suds.client import Client


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.24.3//api/soap/mantisconnect.php?wsdl")
        # try - if login failed
        try:
            # mc_login - operation name
            client.service.mc_login("administrator", "root")
            return True
        except WebFault:
            return False
