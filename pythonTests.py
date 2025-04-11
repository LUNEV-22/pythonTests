import pytest
import sys

def check(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Тесты

def standart():
    assert check("A man a plan a canal Panama") == True

def none():
    assert check("Hello World") == False

def edge():
    assert check("") == True
    assert check("A") == True
    assert check("12321") == True

def registr():
    assert check("RaceCar") == True

def special():
    assert check("Madam, I'm Adam") == True

if __name__ == "__main__":
    print("Тест 'Madam':", check("Madam"))  
    print("Тест 'Python':", check("Python"))  
    
    with open('test_results.txt', 'w') as f:
        original_stdout = sys.stdout
        sys.stdout = f
        
        pytest_args = [__file__, "-v"]
        exit_code = pytest.main(pytest_args)
        
        sys.stdout = original_stdout
    
    with open('test_results.txt', 'r') as f:
        print("\nРезультаты тестов:\n" + f.read())

    sys.exit(exit_code)
