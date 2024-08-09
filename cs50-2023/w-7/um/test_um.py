import pytest
from um import count
def main():
    test()
def test():
    assert count("um")==1
    assert count("UM")==1
    assert count("yUM")==0
    assert count ("yum yum")==0
    assert count ("um, ok, Um")==2

if __name__=="__main__":
    main()