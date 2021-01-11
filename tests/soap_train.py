from suds.client import Client
from suds import WebFault


def adk():
    client = Client("http://localhost/mantisbt-2.24.3//api/soap/mantisconnect.php?wsdl")
    try:
        client.service.mc_login("administrator", "root")
        return True
    except WebFault:
        return False


print(adk())