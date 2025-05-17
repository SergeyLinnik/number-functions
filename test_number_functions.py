from number_functions import max_number

def test_max_number():
    # Тестирование разных пар чисел
    assert max_number(5, 3) == 5
    assert max_number(-1, 1) == 1
    assert max_number(0, 0) == 0  # Одинаковые числа
    assert max_number(3.5, 2.9) == 3.5
    assert max_number(-10, -20) == -10
    
    print("Все тесты для max_number() пройдены успешно!")

if __name__ == "__main__":
    test_max_number()
