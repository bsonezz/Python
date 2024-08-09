from bank import value

def test_hello():
    assert value("hello")==0
    assert value("Hello")==0
    assert value("HELLO , WORLD")==0

def test_dal():
    assert value("dalam")==100
    assert value("dal!")==100
    assert value("100")==100
def test_ha():
    assert value("ha...yah!")==20