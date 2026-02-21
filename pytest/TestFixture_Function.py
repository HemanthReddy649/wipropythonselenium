#scope is run before and after every function

import pytest

@pytest.mark.usefixture("openbrowser")
def test_login():
    print("enter the username")
    print("enter the password")
    print("click on the login button")

@pytest.mark.usefixtures("closebrowser")
def test_logout():
    print("User is logged out")

    #fixtures at class level
    #fixtures at module level
    #fixtures at session level
