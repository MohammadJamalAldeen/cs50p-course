from numb3rs import validate


def test_0_9():
    assert validate("-1.7.2.3") == False
    assert validate("0.0.0.0") == True
    assert validate("1.1.1.1") == True
    assert validate("9.1.2.3") == True


def test_10_99():
    assert validate("10.11.98.33") == True
    assert validate("99.66.75.35") == True
    assert validate("50.25.87.62") == True
    assert validate("99.99.99.99") == True


def test_100_199():
    assert validate("100.199.134.198") == True
    assert validate("199.132.175.108") == True
    assert validate("150.170.120.129") == True


def test_200_255():
    assert validate("200.255.243.211") == True
    assert validate("255.233.222.241") == True
    assert validate("256.247.206.221") == False
    assert validate("245.211.244.268") == False


def test_strs():
    assert validate("c.1.1.1") == False
    assert validate("*") == False


def test_zero():
    assert validate("01.002.03.0233") == False
