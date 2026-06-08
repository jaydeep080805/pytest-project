from lib.count_words import count_words
import pytest

def test_count_words_returns_0_when_empty_string_provided():
    result = count_words("")
    assert result == 0

def test_count_words_returns_attribute_error_if_given_int():
    with pytest.raises(AttributeError) as e:
        count_words(1)

    error_message = str(e.value)
    assert error_message == "'int' object has no attribute 'split'"

def test_count_words_returns_1_with_1_word_string():
    result = count_words("word")
    assert result == 1

def test_count_words_returns_5_with_5_word_string():
    result = count_words("This string has 5 words")
    assert result == 5