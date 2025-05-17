from number_functions import max_number, even_numbers

def test_max_number():
    """Тесты для функции max_number()"""
    assert max_number(5, 3) == 5
    assert max_number(-1, 1) == 1
    assert max_number(0, 0) == 0
    assert max_number(3.5, 2.9) == 3.5
    assert max_number(-10, -20) == -10
    print("✓ Все тесты max_number() пройдены")

def test_even_numbers():
    """Тесты для генератора even_numbers()"""
    # Преобразуем генератор в список для проверки
    assert list(even_numbers(10)) == [0, 2, 4, 6, 8, 10]
    assert list(even_numbers(7)) == [0, 2, 4, 6]
    assert list(even_numbers(0)) == [0]
    assert list(even_numbers(-5)) == []
    print("✓ Все тесты even_numbers() пройдены")

def demo_functions():
    """Демонстрация работы всех функций"""
    print("\nДемонстрация работы:")
    print(f"max_number(8, 5) = {max_number(8, 5)}")
    
    print("even_numbers(12):")
    for num in even_numbers(12):
        print(num, end=" ")
    print("\n")

if __name__ == "__main__":
    test_max_number()
    test_even_numbers()
    demo_functions()
