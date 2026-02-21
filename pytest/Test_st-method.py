#used inside the class only
#runs before and after the test methods inside the class
#incase of inheritance set up and  tear downs are applied
class Testclass1:

    #class level set up
    def setup_class(cls):
        print("API Autorization needed with username and password")
    def teardown_class(cls):
        print("API Authorization closed")

    def setup_method(method):
        print("opening the browaer")
    def teardown_method(method):
        print("closing the browser")

    #testcase1
    def testcase1(self):
        print("testcase 1 is executed")

    #testcase2
    def testcase2(self):
        print("test case2 executed")

    # testcase3

    def testcase3(self):
        print("testcase2 executed")

class Testcase2:
    #testcase1
    def testcase1(self):
        print("testcase 1 is executed")

    #testcase2
    def testcase2(self):
        print("test case2 executed")

    # testcase3

    def testcase3(self):
        print("testcase2 executed")


class Testcase2(Testclass1):
    #testcase1
    def testcase1(self):
        print("testcase 1 is executed")

    #testcase2
    def testcase2(self):
        print("test case2 executed")

    # testcase3

    def testcase3(self):
        print("testcase2 executed")