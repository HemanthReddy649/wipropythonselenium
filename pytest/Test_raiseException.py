import pytest

def div(a,b):
    return a/b
def test_div_zero():
    with pytest.raises(ValueError)as exc_info:
        print(exc_info)
        div(5,0)
        assert str(exc_info.value)=="ZeroDivisionError:division by zero"