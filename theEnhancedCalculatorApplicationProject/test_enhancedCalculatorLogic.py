import pytest
from enhancedCalculatorLogic import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_addition(calculator):
    """Test addition functionality."""
    result = calculator.calculate("5+3")
    assert result == "8"


def test_subtraction(calculator):
    """Test subtraction functionality."""
    result = calculator.calculate("10-7")
    assert result == "3"


def test_multiplication(calculator):
    """Test multiplication functionality."""
    result = calculator.calculate("4*5")
    assert result == "20"


def test_division(calculator):
    """Test division functionality."""
    result = calculator.calculate("20/5")
    assert result == "4.0"


def test_division_by_zero(calculator):
    """Test division by zero."""
    result = calculator.calculate("5/0")
    assert result == "Error"


def test_calculate_tip(calculator):
    assert calculator.calculate_tip(100, 0.10) == 10.0  # 10% of 100
    assert calculator.calculate_tip(50, 0.25) == 12.5  # 25% of 50
    assert calculator.calculate_tip(0, 0.15) == 0.0  # 15% of 0


def test_invalid_expression(calculator):
    """Test handling of invalid expressions."""
    result = calculator.calculate("5++3")
    assert result == "Error"

    result = calculator.calculate("abc+5")
    assert result == "Error"