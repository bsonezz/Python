import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("1/100") == 1


def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("23/1")