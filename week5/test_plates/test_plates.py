from plates import is_valid
def test_len():
    assert is_valid("aaa") == True
    assert is_valid("aaadddl") == False
    assert is_valid("") == False
def test_first2() :
    assert is_valid("AA") == True
    assert is_valid("A11") == False
    assert is_valid("00") == False
def  test_nums_in_mid():
    assert is_valid("AB53E") == False
    assert is_valid("CC55D") == False
    assert is_valid("LX55") == True

def test_zero_first() :
    assert is_valid("AB000") == False
    assert is_valid("AC0321") == False
    assert is_valid("AC301") == True

def test_punctuation():
    assert is_valid("aa*a") == False
    assert is_valid("Gaa.") == False
    assert is_valid("aaU50,.") == False

