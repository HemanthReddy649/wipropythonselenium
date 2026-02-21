import pytest
@pytest.fixture(params=["Chrome","Firefox"])
#request - pytest object that contains information about
#who is calling the fixture and with what data
def browser(request):
    if request.params=="Chrome":
        print("Invoke chrome browser")
        return request.param
def testbrowser(browser):
    assert browser in ["chrome","Firefox"]

#selecting even or odd number

