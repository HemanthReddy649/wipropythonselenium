#fixtures are the peice of code which are run before the testcases or after the testcases

import pytest

@pytest.fixture
def simple_data():
    return 45

#test using the simple fixture
def testcase1(simple_data):
    assert simple_data==45

@pytest.fixture()
def api_url():
    return "https://api.example.com"

def test_api(api_url):
    assert "https" in api_url