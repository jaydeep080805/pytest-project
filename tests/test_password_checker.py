from lib.password_checker import PasswordChecker
import pytest

def test_check_returns_true_if_password_length_eight():
    pw = PasswordChecker()
    result = pw.check("12345678")

    assert result == True

def test_check_returns_true_if_password_length_higher_than_eight():
    pw = PasswordChecker()

    result1 = pw.check("123456789")
    result2 = pw.check("abcdefghi")
    result3 = pw.check("abcdefghijkfnsl")

    assert result1 == True
    assert result2 == True
    assert result3 == True

def test_check_returns_exception_if_password_length_lower_than_eight():
    pw = PasswordChecker()

    with pytest.raises(Exception) as e:
        pw.check("123")

    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."