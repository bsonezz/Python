from twttr import shorten

def test_words():
    assert shorten("Twitter") == "Twttr"
    assert shorten("IAnmjlP") == "nmjlP"
def test_wordnum():
    assert shorten("CS50") == "CS50"
def test_num():
    assert shorten("22") == "22"
def test_punctuation():
    assert shorten("'?") == "'?"

