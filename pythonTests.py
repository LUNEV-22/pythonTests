# palindrome_with_tests.py
import pytest

def is_palindrome(s: str) -> bool:
    """Проверяет, является ли строка палиндромом (игнорирует регистр и пробелы)."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Тесты

def test_standard_palindrome():
    assert is_palindrome("A man a plan a canal Panama") == True

def test_non_palindrome():
    assert is_palindrome("Hello World") == False

def test_edge_cases():
    assert is_palindrome("") == True
    assert is_palindrome("A") == True
    assert is_palindrome("12321") == True

def test_case_insensitivity():
    assert is_palindrome("RaceCar") == True

def test_with_special_chars():
    assert is_palindrome("Madam, I'm Adam") == True

if __name__ == "__main__":
    print("Тест 'Madam':", is_palindrome("Madam"))  # True
    print("Тест 'Python':", is_palindrome("Python"))  # False
    pytest.main([__file__, "-v"])
