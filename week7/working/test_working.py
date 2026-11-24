import pytest
from working import convert


def test_cases():
    assert convert("11 AM to 8:50 PM") == "11:00 to 20:50"
    assert convert("12 AM to 8:50 PM") == "00:00 to 20:50"
    assert convert("12:59 AM to 12:50 PM") == "00:59 to 12:50"


def test_invalidtime():
    with pytest.raises(ValueError):
        convert("14 AM to 8:00 PM")
    with pytest.raises(ValueError):
        convert("12:00 AM to 60:50 PM")
    with pytest.raises(ValueError):
        convert("1 AM to 8:70 PM")


def test_invalidperiod():
    with pytest.raises(ValueError):
        convert("11 CM to 8:00 PM")
    with pytest.raises(ValueError):
        convert("1 AM to 8:00 4M")


def test_typo():
    with pytest.raises(ValueError):
        convert("s")
    with pytest.raises(ValueError):
        convert("11 am to 12 pm")
    with pytest.raises(ValueError):
        convert("11 too 12")