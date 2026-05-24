import pytest
import allure

from calculator.calc import Calculator


@pytest.fixture
def calc():
    return Calculator()


@allure.feature("Calculator")
@allure.story("Addition")
def test_add(calc):
    assert calc.add(2, 3) == 5


@allure.feature("Calculator")
@allure.story("Subtraction")
def test_subtract(calc):
    assert calc.subtract(10, 5) == 5


@allure.feature("Calculator")
@allure.story("Multiplication")
def test_multiply(calc):
    assert calc.multiply(4, 5) == 20


@allure.feature("Calculator")
@allure.story("Division")
def test_divide(calc):
    assert calc.divide(20, 5) == 4


@allure.feature("Calculator")
@allure.story("Division By Zero")
def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)
