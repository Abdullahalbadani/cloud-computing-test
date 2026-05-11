import pytest
from app import Calculator, multiply, divide


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
