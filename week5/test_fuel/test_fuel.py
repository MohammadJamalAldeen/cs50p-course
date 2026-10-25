from fuel import convert
from fuel import gauge
import pytest
def test_valueerror():
    with pytest.raises(ValueError):
        convert("m/n")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ValueError):
        convert("-2/-3")
    with pytest.raises(ValueError):
        convert("-2/3")
    with pytest.raises(ValueError):
        convert("2/-3")
    with pytest.raises(ValueError):
        convert("hello")

def test_value():
    assert convert("3/4") == 75
    assert convert("9/9") == 100

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(9) == "9%"
    assert gauge(98) == "98%"




