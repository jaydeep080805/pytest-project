from lib.gratitudes import Gratitudes

def test_gratitudes_list_is_empty_when_instantiated():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

def test_gratitude_adds_to_list_when_provided_with_value():
    gratitudes = Gratitudes()
    gratitudes.add("Coding")

    assert len(gratitudes.gratitudes) == 1
    assert gratitudes.gratitudes == ["Coding"]

def test_gratitute_adds_to_list_when_provided_with_empty_string():
    gratitudes = Gratitudes()
    gratitudes.add("")

    assert len(gratitudes.gratitudes) == 1
    assert gratitudes.gratitudes == [""]

def test_gratitude_adds_to_list_when_given_different_variable_types():
    gratitudes = Gratitudes()

    gratitudes.add("")
    gratitudes.add(5)
    gratitudes.add(5.3)
    gratitudes.add(True)
    gratitudes.add(False)
    gratitudes.add([])
    gratitudes.add({})

    assert len(gratitudes.gratitudes) == 7
    assert gratitudes.gratitudes == ["", 5, 5.3, True, False, [], {}]

def test_format_returns_correct_string_with_one_gratitute():
    gratitudes = Gratitudes()
    gratitudes.add("legs")

    result = gratitudes.format()

    assert result == "Be grateful for: legs"

def test_format_returns_correct_string_with_multiple_gratitutes():
    gratitudes = Gratitudes()
    gratitudes.add("legs")
    gratitudes.add("arms")
    gratitudes.add("eyes")

    result = gratitudes.format()

    assert result == "Be grateful for: legs, arms, eyes"