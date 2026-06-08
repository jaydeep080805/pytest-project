from lib.present import Present
import pytest

def test_contents_returns_none_when_instantiated():
    present = Present()
    assert present.contents == None

def test_wrap_throws_exception_when_contents_is_not_none():
    present = Present()
    present.contents = "value"

    with pytest.raises(Exception) as e:
        present.wrap("")

    # error message has to be cast back to string
    # or else the type of the message will be a type <class>
    # and the assertion will fail
    error_message = str(e.value)
    # print(type(e.value))
    
    assert error_message == "A contents has already been wrapped."

def test_wrap_sets_content_when_contents_is_none():
    present = Present()
    present.wrap("toy")
    assert present.contents == "toy"


def test_unwrap_throws_exception_if_contents_is_none():
    present = Present()
    
    with pytest.raises(Exception) as e:
        present.unwrap()

    error_message = str(e.value)

    assert error_message == "No contents have been wrapped."

def test_unwrap_returns_content_when_provided_with_content():
    present = Present()

    present.wrap("toy")
    result = present.unwrap()

    assert result == "toy"