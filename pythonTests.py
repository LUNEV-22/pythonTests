
import pytest
import sys

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
    
    # Запуск тестов с сохранением результатов в файл
    with open('test_results.txt', 'w') as f:
        # Перенаправляем вывод в файл
        original_stdout = sys.stdout
        sys.stdout = f
        
        # Запуск pytest с аргументами
        pytest_args = [__file__, "-v"]
        exit_code = pytest.main(pytest_args)
        
        # Восстанавливаем стандартный вывод
        sys.stdout = original_stdout
    
    # Дублируем результаты в консоль
    with open('test_results.txt', 'r') as f:
        print("\nРезультаты тестов:\n" + f.read())
    
    # Завершаем с соответствующим кодом
    sys.exit(exit_code)
