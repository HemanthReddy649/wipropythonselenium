# grouping - set of testcases run together - issues fix in that module

import pytest
# testcase 1
def testcase1():
    print("Testcase1 is executed")

# testcase 2
@pytest.mark.sanity
def testcase2():
    print("Testcase2 is executed")

# testcase 3
@pytest.mark.regression
def testcase3():
    print("Testcase3 is executed")