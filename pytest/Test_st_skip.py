#skip - if defects are there
#skip - if the testcases are absoulte
#windows , mobile -os dependency
#browsers - FF,IE,chrome

import pytest
#testcases1
def testcase1():
    print("Testcase1 is executed")

#testcase2
@pytest.mark.skip
def testcase2():
    print("testcase2 is executed")
def testcase3():
    print("testcase3 is executed")
