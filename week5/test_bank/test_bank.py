from bank import value
def test_basic():
    assert value("hello") == 0
    assert value("h") == 20
    assert value("b") == 100
def test_capital():
    assert value("Hello") == 0
    assert value("H") == 20
    assert value("B") == 100
def test_space():
    assert value("   hello     MMM") == 0
    assert value("hEY  SHKJJB") == 20
    assert value(" B  ") == 100