
import pytest

from Test_SimpleFixture import api_url

#testcases1
def testcase1():
    print("Testcase1 is executed ")

#testcase2
def testcase2():

    print("Testcase2 is executed")

#testcase3

def testcase3():
    print("Testcase3 is executed")

def testcase4():
    print("Testcase3 is executed")

def testcase5():
    print("Testcase3 is executed")

def test_login():
    print("Login test is executed")

def test_api(api_url):
    assert "https" in api_url