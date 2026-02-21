# The conftest.py file in pytest serves as a local, per-directory plugin that is automatically discovered and
# used by tests within its directory and subdirectories

import pytest


@pytest.fixture
def simple_data():
    return 45


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    print("Current browser:", request.param)
    return request.param


@pytest.fixture()
def api_url():
    return "https://api.example.com"


@pytest.fixture(scope='function')
def openbrowser():
    # precondition
    print("open the browser")


@pytest.fixture(scope='function')
def closebrowser():
    # post condition
    print("closing the browser")


@pytest.fixture(scope="class")
# when we use yeild - automatic teardown is happening
def dbconnection():
    # precondition
    print("open the db connection")  # code before the yield - set up
    yield
    print("closing the db conenction")  # code after the yield - teardpwn


@pytest.fixture
def setup():
    print("Setup")
    return "data"

# v when we use return the automatice tear down will not happen

@pytest.fixture(scope = "module")
def setupapi():
    print("Authorize apis with username and password") # setup
    yield
    print("Unauthorize apis with username and password") # tear do

@pytest.fixture(scope = "session")
def sessionsetup():
    print("Tests started on QA environment ") # setup
    yield
    print("Tests finished on QA environment") # tear down



@pytest.fixture()
def fixture_a():
    return "Data from A"

@pytest.fixture()
def fixture_b(fixture_a): # calling another fixture
    return f"{fixture_a} + Data from B"