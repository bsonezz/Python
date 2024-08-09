from plates import is_valid

def test_1():
    assert is_valid("CS50")==True
    assert is_valid("CS05")==False
    assert is_valid("C")==False
def test_2():
    assert is_valid("CS50P")==False
    assert is_valid("PI3.14")==False
def test_3():
    assert is_valid("H")==False
    assert is_valid("OUTATIME")==False
    assert is_valid("0UTATIME")==False
    assert is_valid("50O")==False
    assert is_valid("05")==False
    assert is_valid("123")==False
    assert is_valid("1234567")==False




