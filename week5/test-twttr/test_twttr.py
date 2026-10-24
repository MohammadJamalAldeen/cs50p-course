from twttr import shorten
def test_capital_strings():
    assert shorten("read") == "rd"
    assert shorten("asuoi") == "s"
def test_small_strings():
    assert shorten("RAUEIDHUI") == "RDH"
def test_numbres():
    assert shorten("123") =="123"
def test_punctuation():
    assert shorten(":;*&^%$#@!~><?}{][^") == ":;*&^%$#@!~><?}{][^"