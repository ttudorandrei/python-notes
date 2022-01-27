# PyTest
from unit_testing.simplecalc import SimpleCalc
import pytest

@pytest.fixture
def calc():
    print("Initiated tests")

def test_calc_add():
    calc = SimpleCalc()
    assert calc.add(2, 6) == 8


def test_calc_subtract():
    calc = SimpleCalc()
    assert calc.subtract(10, 4) == 6


def test_calc_multiply():
    calc = SimpleCalc()
    # assert calc.multiply(3, 6) == 18
    # result of multiplication would be -32.3600000000001 and not a perfect match to -32.36
    # so we use the approx method to approximate the result
    assert pytest.approx(calc.multiply(0.4, -80.9)) == -32.36


def test_calc_divide():
    calc = SimpleCalc()
    assert calc.divide(6, 3) == 2


# this will use a context manager (keyword: with)
def test_calc_divide_by_zero_raises_error():
    # context manager = with
    with pytest.raises(ZeroDivisionError):
        calc = SimpleCalc()
        calc.divide(1, 0)
