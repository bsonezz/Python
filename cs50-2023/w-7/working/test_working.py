import pytest
from working import convert

def main():
    test()

def test():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    assert convert("10 AM to 3 PM") == "10:00 to 15:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

if __name__ == "__main__":
    main()
