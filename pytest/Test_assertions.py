#basic assertion
#hard assertions - this will stop the execution of the testcase /est suite
#soft assertions will continue to run even if the assertion fails

#basic assertions
import pytest_check as check
def test_add():
    result = 2+3
    assert result==5

#checking true or false

def test_boolean():
    assert True
    assert not False

#none value
def test_none():
    value=None
    assert value is None

#list assertion comparision
def test_list():
    fruits=["apple","banana","orange"]
    assert "banana" in fruits
#dictionary assertions
def test_dict():
    creds={
        "username":"Admin",
        "password":"admin123"

    }
    assert creds["password"]=="admin123"
  #comparing lists
def test_comparelist():
    assert [1234]==[1234]

#assertions with custom message
def test_custommsg():
    result=10
    assert result == 10,"Result should be 5"

#soft assertions

def test_multiple():
    check.equal(1,2)
    check.equal(3,3)



