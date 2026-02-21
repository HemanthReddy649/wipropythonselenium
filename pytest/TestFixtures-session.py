#session - runs once for the entire pytest run
#global configuration

import pytest

@pytest.mark.usefixtures("sessionsetup")
def test_one():
    print("Testcase1")
def test_two():
    print("Testcase2")