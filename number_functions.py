def max_number(a, b):
    """Возвращает максимальное из двух чисел без использования встроенной max()"""
    return a if a > b else b

def empty_function():
    """Пустая функция"""
    pass

def even_numbers(n):
    """Генератор четных чисел от 0 до n включительно"""
    for i in range(0, n + 1, 2):
        yield i
