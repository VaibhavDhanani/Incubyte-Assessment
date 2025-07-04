from string_calculator import StringCalculator
import pytest

@pytest.fixture
def string_calculator():
    return StringCalculator()



def test_add_empty_string(string_calculator):
    assert string_calculator.add("") == 0
    