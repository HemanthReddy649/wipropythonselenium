#function level set up and tear down
#these run before and after each test function

#set up at function level
import pytest
def setup_function(function):
    print("Opening the browser")

    #teardown_function(function)
def teardown_function(function):
    print("closing the browser")

def testcase1():
    print("Testcase1 is executed")

def testcase2():
    print("Testcase2 is executed")


def testcase3():
    print("Testcase3 is executed")