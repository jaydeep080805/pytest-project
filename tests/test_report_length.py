from lib.report_length import report_length

def test_report_length_hello_returns_five():
    assert report_length("hello") == "This string was 5 characters long."
    assert report_length("bye bye") == "This string was 7 characters long."
    assert report_length("bonjour") == "This string was 7 characters long."
    assert report_length("test") == "This string was 4 characters long."
    assert report_length("three") == "This string was 5 characters long."