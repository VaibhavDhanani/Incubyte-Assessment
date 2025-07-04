from string_calculator import StringCalculator
import pytest

@pytest.fixture
def string_calculator():
    return StringCalculator()



def test_add_empty_string(string_calculator):
    assert string_calculator.add("") == 0
    
def test_add_single_number(string_calculator):
    assert string_calculator.add("2") == 2
    
    
def test_add_two_or_three_numbers(string_calculator):
    assert string_calculator.add("2,3") == 5
    assert string_calculator.add("1,2,3") == 6
    assert string_calculator.add("4,5,6") == 15