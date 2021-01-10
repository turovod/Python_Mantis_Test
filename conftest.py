import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app():
    global fixture
    if fixture is None or not fixture.is_valid():
        fixture = Application()
    return fixture


# Common destroy fixture for all tests
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        # fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
