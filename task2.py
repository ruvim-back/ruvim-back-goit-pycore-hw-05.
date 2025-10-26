import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор, що знаходить всі дійсні числа у тексті та повертає їх по одному.
    """
    pattern = r"\d+\.\d+|\d+"  # знаходить як цілі, так і дробові числа
    for number in re.findall(pattern, text):
        yield float(number)


def sum_profit(text: str, func: Callable) -> float:
    """
    Повертає суму всіх дійсних чисел з тексту, використовуючи функцію-генератор.
    """
    return sum(func(text))
