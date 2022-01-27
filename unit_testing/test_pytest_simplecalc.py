# PyTest
from unit_testing.simplecalc import SimpleCalc


def test_calc_add():
    calc = SimpleCalc()
    assert calc.add(2, 6) == 8


def test_calc_subtract():
    calc = SimpleCalc()
    assert calc.subtract(10, 4) == 6


def test_calc_multiply():
    calc = SimpleCalc()
    assert calc.multiply(3, 6) == 18


def test_calc_divide():
    calc = SimpleCalc()
    assert calc.divide(6, 3) == 2
