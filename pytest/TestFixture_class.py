import pytest

@pytest.mark.usefixtures("dbconnection")
class TestLogin:

    def test_login(self):
        print("enter the username")
        print("enter the password")
        print("click on the login button")

    def test_logout(self):
        print("user is logged out")
