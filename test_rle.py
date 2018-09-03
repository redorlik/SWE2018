from rle import rle_encoder

def test_simple():
    assert rle_encoder("bbbkkk") == "b3k3"
def test_advanced():
    assert rle_encoder("ffffiiiii") == "f4i5"
