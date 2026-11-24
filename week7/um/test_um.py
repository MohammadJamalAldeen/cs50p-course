from um import count
def test_case():
    assert count("hello , UM , I hate coffe") == 1
    assert count("UM , um , I hate coffe") == 2

def test_inside_word():
    assert count("hello , um , I like meat yummy") == 1
    assert count("UMU is the name of my uni") == 0



def test_punctuation():
    assert count("hello  ,um, could you please give me your bike") == 1
