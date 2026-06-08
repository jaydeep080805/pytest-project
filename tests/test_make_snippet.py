from lib.make_snippet import make_snippet

def test_make_snippet_returns_empty_string_when_provided_no_value():
    result = make_snippet("")
    assert result == ""


def test_make_snippet_returns_all_words_if_less_than_5_words_provided():
    result = make_snippet("Less than 3")
    assert result == "Less than 3"

def test_make_snippet_returns_all_words_5_words_provided():
    result = make_snippet("This string has 5 words")
    assert result == "This string has 5 words"


def test_make_snippet_returns_5_words_with_ellipses_if_more_than_5_words_provided():
    result = make_snippet("This string has more than 5 words")
    assert result == "This string has more than..."
