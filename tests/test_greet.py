from lib.greet import greet

def test_greet_with_jay():
    result = greet("jay")
    assert result == "Hello, jay!"