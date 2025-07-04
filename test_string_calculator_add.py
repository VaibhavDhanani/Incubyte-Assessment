import re
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
    
    
def test_add_unknown_numbers(string_calculator):
    assert string_calculator.add("1,2,3,4,5,6,7,8,9") == 45
    assert string_calculator.add("10,20,30,40,50,60,70,80,90,100") == 550
    assert string_calculator.add("1,2,3,6,5,4") == 21
    
    
def test_add_handles_newline_characters(string_calculator):
    assert string_calculator.add("1\n2,3\n4,5,6,7,8,9") == 45
    assert string_calculator.add("1\n2\n3\n6\n\n\n5\n4") == 21
    
    
def test_add_handles_custom_delimiter(string_calculator):
    assert string_calculator.add("//;\n1;2;3;4;5;6;7;8;9") == 45
    assert string_calculator.add("//#\n1#2#3#6#5#4") == 21
    assert string_calculator.add("//#\n10") == 10
    
    
def test_add_handling_negative_number(string_calculator):
    with pytest.raises(ValueError,match="negatives not allowed"):
        string_calculator.add("1,2,-3")
        
    with pytest.raises(ValueError,match="negatives not allowed"):
        string_calculator.add("//;\n\n1;2;3\n\n\n-4\n5")
        
        
        
def test_add_handling_multiple_negative_numbers(string_calculator):
    with pytest.raises(ValueError,match=re.escape("negatives not allowed : [-2, -3]")):
        string_calculator.add("1,-2,-3")
        
    with pytest.raises(ValueError,match=re.escape("negatives not allowed : [-2, -4, -5]")):
        string_calculator.add("//;\n\n1;-2;3\n\n\n-4\n-5")
        
        
def test_add_counting_times_method_called(string_calculator):
    string_calculator.add("1,2,3")
    assert string_calculator.get_called_count() == 1
    string_calculator.add("1,2,3,4")
    string_calculator.add("1,2,3,5")
    string_calculator.add("1")
    assert string_calculator.get_called_count() == 4
    