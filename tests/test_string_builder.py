import pytest
from lib.string_builder import *

def test_default_string_is_empty():
    sb = StringBuilder()

    assert sb.str == ""

def test_add_function_adds_words_to_string():
    sb = StringBuilder()    
    sb.add("test string")

    assert sb.str == "test string"

def test_add_function_with_multiple_strings():
    sb = StringBuilder()
    sb.add("does ")
    sb.add("this ")
    sb.add("add ")
    sb.add("correctly?")

    assert sb.str == "does this add correctly?"

def test_add_function_with_multiple_strings_and_error():
    sb = StringBuilder()
    sb.add("does ")
    sb.add("this ")

    with pytest.raises(TypeError) as error:
        sb.add(8)

    sb.add("add ")
    sb.add("correctly?")

    assert sb.str == "does this add correctly?"


def test_add_function_returns_error_when_adding_different_data_types():
    sb = StringBuilder()    
    
    with pytest.raises(TypeError) as error:
        sb.add(39)

def test_size_returns_five_when_five_letter_word_input():
    sb = StringBuilder()
    sb.add("words")

    assert sb.size() == 5

def test_size_returns_ten_when_word_with_whitespace_entered():
    sb = StringBuilder()
    sb.add("ten letter")
    
    assert sb.size() == 10

def test_size_returns_4_when_error_caught():
    sb = StringBuilder()
    sb.add("te")
    
    with pytest.raises(TypeError) as error:
        sb.add(2390)

    sb.add("st")

    assert sb.str == "test"

def test_output_returns_red_when_red_input():
    sb = StringBuilder()
    sb.add("red")

    assert sb.output() == "red"

def test_word_with_different_cases_returns_correct_case():
    sb = StringBuilder()
    sb.add("Test tHat THiS stRINg RemainS iN iTS original case")

    assert sb.output() == "Test tHat THiS stRINg RemainS iN iTS original case"