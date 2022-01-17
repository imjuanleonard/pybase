from pybase.factorial import fac


def test_factorial():
    assert fac(0) == 1
    assert fac(1) == 1
    assert fac(2) == 2
    assert fac(3) == 6
    assert fac(4) == 24
    assert fac(5) == 120
