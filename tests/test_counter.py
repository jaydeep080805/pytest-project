from lib.counter import *

def test_default_count_value():
    counter = Counter()
    assert counter.count == 0

def test_count_increases_by_one():
    counter = Counter()
    counter.add(1)
    assert counter.count == 1

def test_count_increases_by_50():
    counter = Counter()
    counter.add(50)
    assert counter.count == 50

def test_counter_returns_correct_value_when_multiple_positive_values_added():
    counter = Counter()
    counter.add(10)
    counter.add(25)
    counter.add(119)

    assert counter.count == 154

def test_counter_returns_correct_value_when_multiple_negative_values_added():
    counter = Counter()
    counter.add(-10)
    counter.add(-25)
    counter.add(-119)

    assert counter.count == -154

def test_counter_returns_correct_value_when_multiple_mixed_values_added():
    counter = Counter()
    counter.add(-10)
    counter.add(25)
    counter.add(-119)

    assert counter.count == -104

def test_counter_decrease_by_1_returns_negative_number():
    counter = Counter()
    counter.add(-1)
    assert counter.count == -1

def test_counter_decrease_by_50_returns_negative_number():
    counter = Counter()
    counter.add(-50)
    assert counter.count == -50

def test_counter_report_returns_string_with_0_value():
    counter = Counter()

    assert counter.report() == "Counted to 0 so far."

def test_counter_report_returns_string_with_50_value():
    counter = Counter()
    counter.add(50)

    assert counter.report() == "Counted to 50 so far."


def test_counter_report_returns_string_with_negative_value():
    counter = Counter()
    counter.add(-50)

    assert counter.report() == "Counted to -50 so far."
