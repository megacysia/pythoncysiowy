from twtrr import shorten

def test_shorten():
    assert shorten("cat") == "ct"